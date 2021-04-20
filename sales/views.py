from django.shortcuts import render

# Create your views here.
#function views are more readable than class views
def home_view(request):
    return render(request,'sales/main.html',{})