# step 4.1: create forms.py, create class and assign forms.filefield to user_image.



from django import forms



class ProfileForm(forms.Form):
    user_image = forms.FileField()
