# step 1.3: define a review in views.py file.
# Step 2.2: add the created html file to views.py to render
# step 5.3: as we get GET and POST in the same url, we need to identify using IF statment and redirect to thankyou.html, we can also render inside if statment 
#           but it is not a good pratice. create a seperate function for thankyou and render the html page there.
# step 5.4: inclding HttpResponceRedirect we can add the extension url over there.
# step 6.2: call the created form class inside view.py forms.ReviewForm now, validate post or get method, also is_valid is a inbuilt method in forms, render the html 
            # nested if is used to check post, get and is_valid
# 






from django.http import HttpResponseRedirect
from django.shortcuts import render
from .import forms

# Create your views here.


def review(request):
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thankyou")

    form = forms.ReviewForm()

    return render (request, "review/review.html", {
        "form": form
    })



def thankyou(request):
    return render(request, "review/thankyou.html")