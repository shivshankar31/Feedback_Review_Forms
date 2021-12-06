# step 1.3: define a review in views.py file.
# Step 2.2: add the created html file to views.py to render



from django.shortcuts import render

# Create your views here.


def review(request):
    return render (request, "review/review.html")