from django import forms

class SendCommentForm(forms.Form):
    content = forms.CharField(label = u'content', required = True, max_length = 1000)

    
    
