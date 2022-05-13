from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from testapp.models import Project

from testapp.forms import Project_form

# Create your views here.
def Home(request):
    if request.method =="GET":
        S = Project_form()
        dict = {"X":S}
        return render(request,"home.html",dict)
    else:
        D = Project_form(request.POST)
        if D.is_valid():
            D.save()
            return redirect("welldone")
def show(request):
    L = Project.objects.all()
    return render(request,"show.html",{"I":L})

def update(request,id):
    if request.method =="GET":
        X = Project.objects.get(id = id)
        U = Project_form(instance=X)
        return render(request,"Home.html",{"X":U})
    else:
        T = Project.objects.get(id = id)
        A = Project_form(request.POST, instance=T)
        if A.is_valid():
            A.save()
            return redirect("welldone")
def remove(request,id):
    if request.method == "GET":
        data = Project.objects.get(id=id)
        Project.delete(data)
        return redirect("welldone")

def card(request,id):
    if request.method =='GET':
        F = Project.objects.get(id=id)
        return render(request,'show.html',{'B':F})
            

@login_required(login_url='login')
def Page2(request):
    return render(request,'page2.html')

@login_required(login_url='login')
def Page3(request):
    return render(request , 'page3.html')

@login_required(login_url='login')
def Page4(request):
    return render(request, 'page4.html')

@login_required(login_url='login')
def Page5(request):
    return render(request , 'page5.html')

@login_required(login_url='login')
def Page6(request):
    return render(request, 'page6.html')
    
    
def register(request):
    if request.method =="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['con_password']
        
        if password == con_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User already Existst")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Existst")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request,"Password doesnot matching...........")
            return redirect('register')
    else:
        return render(request,"register.html")
    
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
        else:
            messages.info(request,'Incorrect username/Password')
            return redirect('login')
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('login')

    