from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import course





# Create your views here.
def index(request):
    courses=course.objects.all()
     
    
    
    
    return render(request,'index.html')
 

def registration(request):
    
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'password mismatch')
            return redirect('registration')
    else:
        return render(request,'registration.html')
    

          

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    courses=course.objects.get(id=pk)

    return render( request,'post.html',{'courses':courses})






def blog(request):
    courses=course.objects.all()
    
    

    
    return render(request,'blog.html',{'courses':courses})





def images(request):
    courses=course.objects.all()
    
    return render(request,'images.html',{'courses':courses})