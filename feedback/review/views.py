# step 1.3: define a review in views.py file.
# Step 2.2: add the created html file to views.py to render
# step 5.3: as we get GET and POST in the same url, we need to identify using IF statment and redirect to thankyou.html, we can also render inside if statment 
#           but it is not a good pratice. create a seperate function for thankyou and render the html page there.
# step 5.4: inclding HttpResponceRedirect we can add the extension url over there.
# step 6.2: call the created form class inside view.py forms.ReviewForm now, validate post or get method, also is_valid is a inbuilt method in forms, render the html 
            # nested if is used to check post, get and is_valid
# step 15.1: remove all cleaned data and save the form, model will save the data and save that to DB.
# step 16.1: in views.py, import django.view Views and create class ReviewView(View), and create get and post function.
# step 17.3: In views.py, post function return HttpResponceRedirect fixed
# step 18.1: import - from django.views.generic.base import TemplateView
# step 18.2: in views.py, remove thankyou function and create ThankyouView class and call TemplateView as arg
# step 18.3: use the keyword template_name to render the html page, no need to use retutn or render methods, 
# step 18.4: we can convert static to dynamic HTML page using predefind get_context_data function
# step 19.2: In views.py, create a new class ReviewList and pass TemplateView argument.
# step 19.3: assign template_name and call get_context_data function, now call objects.all() and populate the data.
# step 20.2: In views.py, create class for detailview and assign the template_name, call get_context_data function, use **kwargs from the function in get() populate the id using primarykey (Pk)
# step 20.1: In views.py, import "from django.views.generic import ListView" 
# step 20.2: create a class with ListView and assign the html, assign model = Review (model class name), this will populate the list, but change the for loop to "object_list". if you like to user alis name use context_object_name varibal and assign the prefered name.
# step 21.1: import DetailView form django.views.generic 
# step 21.2: In views.py, create new class and user DetailView as arg, template_name, model need to assign.
# step 22.1: In views.py, add from django.views.generic.edit import FormView
# step 22.2: create class and use FormVIew also use form_class, template_name and success_url. To save form user form valid function and save the form.





from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormView

# from feedback.review.models import Review
from .forms import ReviewForm
from .models import Review
from django.views import View


# Create your views here.

class ReviewView(FormView): 
    form_class = ReviewForm
    template_name = 'review/review.html'
    success_url = 'thankyou'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# method 1: for get and post
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, 'review/review.html',{
#             'form': form
#         })
    
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thankyou')
            
#         return render(request, 'review/review.html', {
#                 'form': form
#             })



# method 1 create class and def function 
# class ThankyouView(View):
#      def get(self,request):
#         return render(request, "review/thankyou.html")



# method 2: import TemplateView
class ThankyouView(TemplateView):
    template_name = 'review/thankyou.html'

    def get_context_data(self, **kwargs):
        context1 = super().get_context_data(**kwargs)
        context1 ['message'] = 'Thank you once again!'
        return context1



# method 1: list view
# class ReviewList(TemplateView):
#     template_name = 'review/reviewlist.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviewlist = Review.objects.all()
#         context ['reviews'] = reviewlist
#         return context



# method 2: list view using ListView method.
class ReviewList(ListView):
    template_name = 'review/reviewlist.html'
    model = Review # you have change the name to "object_list" in html page.
    context_object_name = 'reviews' #you can give you own name using this variable.




# method 1: detail view
# class ReviewDetailview(TemplateView):
#     template_name = 'review/details.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         revied_id = kwargs['id']
#         detailview = Review.objects.get(pk=revied_id) # pk = primarykey
#         context ['reviewdetail'] = detailview
#         return context

# method 2: detail view using DetailView
class ReviewDetailview(DetailView):
    template_name = 'review/details.html'
    model = Review # you can use "object"
    context_object_name = 'reviewdetail' # if you like to user alise name insted of object. you can use this.




# def review(request):
#     if request.method == "POST": # this workd if its a POST method or not
#         form = forms.ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # review_data = Review(user_name = form.cleaned_data['user_name'], review_text = form.cleaned_data['feedback'], rating = form.cleaned_data['rating'])
#             # review_data.save()
#             # print(form.cleaned_data)
#             return HttpResponseRedirect("/thankyou")
#     else: # this part works if its GET metnod
#         form = forms.ReviewForm()

#     return render (request, "review/review.html", {
#         "form": form
#     })


# def thankyou(request):
#     return render(request, "review/thankyou.html")