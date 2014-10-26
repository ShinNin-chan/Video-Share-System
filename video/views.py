from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext 
from video.form import UploadFileForm, SendCommentForm, RatingForm
from video.models import Video,Comment
from django.contrib.auth.decorators import login_required  


@login_required
def upload(request):
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
    return render_to_response('upload.html', {'form': form},context_instance=RequestContext(request))

def uploadSuccess(request):
    return render_to_response('upload_Success.html',context_instance=RequestContext(request))


def video_play(request,video_id):
    video_object = Video.objects.get(id=video_id)
    video_path = video_object.file.url
    HasRated = False
    
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

