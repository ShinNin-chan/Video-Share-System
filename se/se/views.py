import account.views
from django.shortcuts import render_to_response

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
        
def personalPage(request):

    return render_to_response('personalPage.html', locals())

def timeLine(request):
    return render_to_response('timeLine.html', locals())




