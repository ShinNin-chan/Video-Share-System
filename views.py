import account.views
from django.shortcuts import render_to_response
from video.models import Video 
from django.template import RequestContext 
from django.contrib.auth.models import User
from friendpair.models import FriendPair
from django.http import HttpResponseRedirect, HttpResponse
import se.forms


class SignupView(account.views.SignupView):
    form_class = se.forms.SignupForm

    def after_signup(self, form):
        self.create_profile(form)
        super(SignupView, self).after_signup(form)

    def create_profile(self, form):
        profile = self.created_user.get_profile()
        profile.birthdate = form.cleaned_data["birthdate"]
        profile.save()
       
class SettingsView(account.views.SettingsView):

    form_class = se.forms.SettingsForm
        
    def update_settings(self, form):
        self.update_info(form)
        super(SettingsView, self).update_settings(form)

    def update_info(self, form):
        if 'birthdate' in form.cleaned_data:
            profile = self.request.user.userprofile
            profile.birthday = form.cleaned_data['birthdate']
            profile.save()

    def get_initial(self):
        initial = super(SettingsView, self).get_initial()
        initial['birthdate'] = self.request.user.userprofile.birthday
        return initial
        

def personalPage(request,user_id = 0):
    
    if user_id == 0 or int(user_id) == request.user.id:
        page_owner = request.user
        flag = 0     # This is my own homepage
    else:
        page_owner = User.objects.get(id = int(user_id))
        if FriendPair.objects.filter(follower = request.user, master = page_owner).count() != 0:
            flag = 1 # already followed
        else:
            flag = 2 # have not yet followed


    videos = Video.objects.filter(owner=page_owner)

    if request.method == 'POST':
        pair = FriendPair()
        pair.follower = request.user
        pair.master = page_owner
        if FriendPair.objects.filter(follower = request.user, master = page_owner).count() == 0:
            pair.save()
        return HttpResponseRedirect('/personalPage/{}'.format(user_id))

    return render_to_response('personalPage.html', locals(),context_instance=RequestContext(request))

def personalPageUnfollow(request,user_id=0):
    if request.method == 'POST':
        if user_id == 0 or int(user_id) == request.user.id:
            page_owner = request.user
            flag = 0     # This is my own homepage
        else:
            page_owner = User.objects.get(id = int(user_id))
        pair = FriendPair.objects.filter(follower = request.user, master = page_owner)[0]
        pair.delete()
    return HttpResponseRedirect('/personalPage/{}'.format(user_id))
    


def timeline(request):
    user = request.user
    relationships = FriendPair.objects.filter(follower = user)
    masters = [pair.master for pair in relationships]
    videos = Video.objects.filter(owner__in=masters)
    videos = sorted(videos,key=lambda v:v.uploadtime,reverse=True)
    return render_to_response('timeLine.html', locals(),context_instance=RequestContext(request))

def timelineall(request):
    videos = Video.objects.all()
    return render_to_response('timeLine.html', locals(),context_instance=RequestContext(request))

