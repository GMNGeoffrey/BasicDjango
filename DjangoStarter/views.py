from django.http import HttpResponse, Http404
from django.shortcuts import render
#from django.contrib import auth #Useful if you want Users
#from django.db.models import Q #Useful if you want complex database queries.



#The following is a basic "view" function.
# The key idea is that you take a "request" and return an HttpResponse
def basic_view(request):
 return HttpResponse("Hello world!")



def view_with_vars(request):
 #With a basic dictionary, you can supply a template with variables!
 myDict = {
   "my_template_var":"This is the value of my_template_var"
 }
 #The "render" shortcut allows us to incorporate variables and templates into
 # our HttpResponse cleanly and elegantly.
 return render(request, "my_template.html", myDict)



#Take a look at "urls.py" to see what my_url_var is passed as.
def url_view(request, my_url_var):
 return render(request, "my_url_based_template.html", {
    "my_url_var":my_url_var
 })

