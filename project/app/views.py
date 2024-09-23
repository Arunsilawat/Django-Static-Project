from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')
   
def login(request):
    if request.method=='POST':
        email1=request.POST.get('email')
        password1=request.POST.get('password')
        # print(email,password)
        fname=request.COOKIES['fname']
        lname=request.COOKIES['lname']
        email=request.COOKIES['email']
        password=request.COOKIES['password']
        if email1==email:
            if password1==password:
                data={'fname':fname,
                      'lname':lname,
                      'email':email,
                      'password':password
                      }
                return render(request,'home.html',data)
            else:
                msg='password not matched'
                return render(request,'home.html',{'msg':msg})
                

        else:
            msg='email id not register'
            return render(request,'home.html',{'msg':msg})
    else:
        return render(request,'home.html')

def registerdata(request):
  

    cstoken=request.POST.get('csrfmiddlewaretoken')
    fname=request.POST.get('firstName')
    lname=request.POST.get('lastName')
    email=request.POST.get('email')
    password=request.POST.get('password')

 
    response=render(request,'home.html')
    response.set_cookie('fname',fname)
    response.set_cookie('lname',lname)
    response.set_cookie('email',email)
    response.set_cookie('password',password)
    return response
