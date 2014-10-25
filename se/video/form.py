from django import forms

class UploadFileForm(forms.Form):
    description = forms.CharField(label = u'description', required = False, max_length = 1000)
    file = forms.FileField()
