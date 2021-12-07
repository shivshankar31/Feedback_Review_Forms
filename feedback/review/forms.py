from django import forms
# step 6.1: create forms.py file and import forms form django, to handle forms and validation automaticly

from django.forms.forms import Form

class ReviewForm(forms.Form):
    user_name = forms.CharField()
