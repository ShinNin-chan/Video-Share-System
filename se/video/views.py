from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext 
from video.form import UploadFileForm
from video.models import Video
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

    video_path = Video.objects.filter(id=video_id)[0].file.file

    return render_to_response('videoplay.html')
