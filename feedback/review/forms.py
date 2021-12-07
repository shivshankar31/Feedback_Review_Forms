# step 6.1: create forms.py file and import forms form django, to handle forms and validation automaticly
# step:8.1: in forms.py, we can chage the lable, max_length, required(*)- by default it set to be true, error_massages






from django import forms
from django.forms.forms import Form





class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=20, required= True, error_messages={
        'required' : 'This field must not be empty',
        'max_length': 'Length of your name should not be more than 20'
    })
