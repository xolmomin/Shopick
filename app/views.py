from django.shortcuts import render



def about(request):
    return render(request,'app/about.html')