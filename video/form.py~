from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(label = u'title', required = True, max_length = 100)
    description = forms.CharField(label = u'description', required = False, max_length = 1000)
    file = forms.FileField()
    
class SendCommentForm(forms.Form):
    content = forms.CharField(label = u'content', required = True, max_length = 1000)

class RatingForm(forms.Form):
    rate = forms.IntegerField(label = u'rate', required = True)    
    
