from django.shortcuts import render

# Create your views here.
def about_view(request, *args , **kwargs ):
    print(args,kwargs)
    print(request.user)
    return render(request,"about.html",{})
    
def contact_view(request , *args , **kwargs):
    return render(request, "contact_view.html" , {})