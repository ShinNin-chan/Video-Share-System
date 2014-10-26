from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext 
from video.form import *
from video.models import Video,Comment
from django.contrib.auth.decorators import login_required  


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


def video_play(request,video_id):
    video_object = Video.objects.get(id=video_id)
    video_path = video_object.file.url
    HasRated = False
    own = True if request.user == video_object.owner else False
    if video_object.rating_person:
        points = round(1.0*video_object.rating_sum/video_object.rating_person,1)
    
    # Handle comment post
    if request.method == 'POST':
        if 'commentsubmit' in request.POST:
            form = SendCommentForm(request.POST)
            if form.is_valid():
                comment = Comment()
                comment.author = request.user
                comment.video = Video.objects.filter(id=video_id)[0]
                comment.content = form.cleaned_data['content']
                comment.save()
                return HttpResponseRedirect('/videoplay/{}'.format(video_id))
        if 'ratingsubmit' in request.POST:
            form = RatingForm(request.POST)
            if form.is_valid():
                video_object.rating_person += 1
                video_object.rating_sum += form.cleaned_data['rate']
                video_object.save()
                HasRated = True
                points = round(1.0*video_object.rating_sum/video_object.rating_person,1)
                render_to_response('videoplay.html', locals(),context_instance=RequestContext(request))
                
                
    else:
        form = SendCommentForm(request.POST)
    
    # Comment display
    commentList = Comment.objects.filter(video=video_object)
      
    # Rate  
    
    
      
    return render_to_response('videoplay.html', locals(),context_instance=RequestContext(request))

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
