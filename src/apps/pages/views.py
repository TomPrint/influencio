from django.shortcuts import render

# Create your views here.

def home(request):

    context = {
        'title':'Strona główna',
      }

    return render (request,'pages/home.html', context)