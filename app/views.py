from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import TodoForm
from .models import Todo

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        user=request.user

        
        todos=Todo.objects.filter(user=user).order_by('priority')
        context={
            
            'todos':todos
        }
        return render(request,'templates/index.html',context)
    else:
        return render(request,'templates/base.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            print(user)
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("Invalid credential")
        
    
    return render(request,'templates/login.html')

def signup_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
            print(username,first_name,email,password,confirmpassword)
            return render(request,'templates/login.html')
    return render(request,'templates/signup.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')

def addtodo(request):
    if request.method =='POST':
        user=request.user
        title=request.POST.get('title')
        status=request.POST.get('status')
        priority=request.POST.get('priority')
        todo=Todo(user=user,title=title,status=status,priority=priority)
        todo.save()
        print(user,title,status,priority)
        return redirect("homepage")
        

    else:
        return HttpResponse("Invalid creadential")

def remove(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('homepage')

def change_status(request,id,status):
    todo=Todo.objects.get(id=id)
    todo.status=status
    todo.save()
    return redirect('homepage')
    