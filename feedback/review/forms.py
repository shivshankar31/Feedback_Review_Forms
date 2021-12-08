# step 6.1: create forms.py file and import forms form django, to handle forms and validation automaticly
# step:8.1: in forms.py, we can chage the lable, max_length, required(*)- by default it set to be true, error_massages
# step 11.1: in forms.py, add feedbask field and rating field.





from typing import Text
from django import forms
from django.forms.forms import Form
from django.forms.widgets import TextInput
from .models import Review





# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=20, required= True, error_messages={
#         'required' : 'This field must not be empty',
#         'max_length': 'Length of your name should not be more than 20'
#     })
#     feedback = forms.CharField(label = 'Your Review', widget = forms.Textarea, max_length= 200)
#     rating = forms.IntegerField(min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = '__all__'
