# step 1.3: define a review in views.py file.
# Step 2.2: add the created html file to views.py to render
# step 5.3: as we get GET and POST in the same url, we need to identify using IF statment and redirect to thankyou.html, we can also render inside if statment 
#           but it is not a good pratice. create a seperate function for thankyou and render the html page there.
# step 5.4: inclding HttpResponceRedirect we can add the extension url over there.


from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def review(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username)
        return HttpResponseRedirect("/thankyou")

    return render (request, "review/review.html")



def thankyou(request):
    return render(request, "review/thankyou.html")