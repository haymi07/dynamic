from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def home(request):
    title = homepage.objects.all().first()

    data = {
        'T':title


    }
    return render(request,'home.html', data)




def experience(request):
     Oldies = Oldies_Day.objects.all()
     workers = workers_day.objects.all()
     Culture = Culture_Day.objects.all()
     pr = prom.objects.all()
     Grad = Graduation.objects.all()
     Exp= Expriance.objects.all()
     data ={
    'old':Oldies,
    'work':workers,
    'culture':Culture,
    'prom':pr,
    'grad':Grad,
    'Expriance':Exp,
    
            }
     return render(request,'experience.html',data)




def future(request):
    futuree = Futures.objects.all().first()

    data = {
        'F':futuree
    }
    return render(request,'future.html',data)




def about(request):
     about_instance = About.objects.first()#.all()

     data = {
        'A':about_instance
    }
     return render(request,'about_us.html',data)





def contact_us(request):
    if request.method =='POST':
      user_name  = request.POST.get('name')
      user_email  = request.POST.get('email')
      user_text  = request.POST.get('text')
   
      obj = contact()
      
      obj.name = user_name
      obj.email =user_email
      obj.text = user_text
      obj.save()
    return render(request, 'contact_us.html')


def oldies(request):
    return render(request,'oldies.html')

def founders(request):
    img = founders.objects.all()
    ob = Titles.objects.all()

    data = {
        'isa':img,
        'obs':ob

    }



    return render(request, 'about_us.html', data)




