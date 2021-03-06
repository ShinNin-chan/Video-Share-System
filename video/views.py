from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext 
from video.form import *
from video.models import Video,Comment


from django.contrib.auth.decorators import login_required 
import json 


@login_required
def upload(request):
    uploadFlag = True
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            video = Video()
            video.owner = request.user
            video.title = form.cleaned_data['title']
            video.file = request.FILES['file']
            video.description = form.cleaned_data["description"]
            video.save()
            return HttpResponseRedirect('success/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', locals(),context_instance=RequestContext(request))

def uploadSuccess(request):
    return render_to_response('upload_Success.html',context_instance=RequestContext(request))



def homepage_video_list(request):
    highscore = Video.objects.all()
    highscore = sorted(highscore, key=lambda x: 1. * x.rating_sum / (1 + x.rating_person))[0:5]
    latest = Video.objects.all()[0:5]
    
    return render_to_response('homepage.html', locals(), context_instance=RequestContext(request))



def video_play(request,video_id):
    video_object = Video.objects.get(id=video_id)
    video_path = video_object.file.url
    own = True if request.user == video_object.owner else False
    if video_object.rating_person:
        points = round(1.0*video_object.rating_sum/video_object.rating_person,1)
    else: 
        points = "Not rated"
    # Comment display
    commentList = Comment.objects.filter(video=video_object).order_by('-time')  
    return render_to_response('videoplay.html', locals(),context_instance=RequestContext(request))



def rate_video(request,video_id):
    
    print request.method, video_id
    if request.method == 'POST':
        print 'hello2'
        form = RatingForm(request.POST)
        if form.is_valid():
            print 'hello3'
            video_object = Video.objects.get(id=video_id)
            video_object.rating_person += 1
            video_object.rating_sum += form.cleaned_data['rate']
            video_object.save()
            HasRated = True
            points = round(1.0*video_object.rating_sum/video_object.rating_person,1)
            return HttpResponse(points)


def comment_video(request, video_id):
    print request.method, video_id
    if request.method == 'POST':
        print "hello2"
        form = SendCommentForm(request.POST)
        if form.is_valid():
            print "hello3"
            comment = Comment()
            comment.author = request.user
            comment.video = Video.objects.filter(id=video_id)[0]
            comment.content = form.cleaned_data['content']
            comment.save()
            print str(comment.author.username), str(comment.time), str(comment.content)
            s = '<p>'+str(comment.author.username)+ comment.time.strftime(" %b. %d, %Y, %I:%m %p ")+ str(comment.content) + '</p>'
            #return HttpResponse(json.dumps({"name":str(comment.author.username), "date":str(comment.time), "content": str(comment.content)}))
            return HttpResponse(s)


def video_modify(request,video_id):
    modifyFlag = True
    video_object = Video.objects.get(id=video_id)
    if request.method == 'POST':
        uploadFlag = True
        form = ModifyVideoForm(request.POST)
        if form.is_valid():
            video_object.title = form.cleaned_data['title']
            video_object.description = form.cleaned_data["description"]
            video_object.save()
            return HttpResponseRedirect('/videoplay/{}'.format(video_id))
    else:
        form = ModifyVideoForm()
    return render_to_response('upload.html', locals(),context_instance=RequestContext(request))
    
    
def video_delete(request,video_id):
    video_object = Video.objects.get(id=video_id)
    video_object.delete()
    return HttpResponseRedirect('/timeline')


def video_share(request,video_id):
    video_object = Video.objects.get(id=video_id)
    video = Video()
    video.owner = request.user
    video.title = video_object.title
    video.file = video_object.file
    video.description = video_object.description
    video.save()
    return HttpResponseRedirect('/videoplay/{}'.format(video_id))
