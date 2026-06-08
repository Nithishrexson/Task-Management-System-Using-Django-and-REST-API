from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def login_(request):
    if request.method == 'POST':
        usname = request.POST['usname']
        psw = request.POST['psw']
        
        user = authenticate(username = usname,password=psw)

        if user:
            login(request,user)
            messages.success(request,'You have logged in successfully')
            return redirect('home')
        else:
            messages.error(request,'Entered username or password is incorrect')
            return redirect('login_')
    return render(request,'login_.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(
            first_name = fname,
            last_name = lname,
            username = uname,
            email = email,
            password = password

        ) 
        return redirect('login_')
    return render(request,'register.html')

def logout_(request):
    logout(request)
    messages.success(request,'You have Logout Successfully')
    return redirect('login_')

def reset_pasw(request):
    data = User.objects.get(username = request.user)
    if request.method == 'POST':
        if 'old_pasw' in request.POST:
            old_pasw = request.POST['old_pasw']
            auth = authenticate(username = data.username,password =old_pasw)

            if auth:
                
                return render(request,'reset_pasw.html',{'new':True})
            else:
                messages.error(request,'Entered password is wrong')
                return redirect('reset_pasw')
            
        if 'new_pasw' in request.POST:
            new_pasw = request.POST['new_pasw']

            data.set_password(new_pasw)
            data.save()
            return redirect('login_')
    return render(request,'reset_pasw.html')


def profile(request):
    data = request.user

    return render(request,'profile.html',{'data':data})

def update(request):
    data = request.user

    data1 = User.objects.get(username = data)

    if request.method == 'POST':
        fstname = request.POST['fstname']
        lstname = request.POST['lstname']
        usrname = request.POST['usrname']
        gmail = request.POST['gmail']

        data1.first_name = fstname
        data1.last_name = lstname
        data1.username = usrname
        data1.email = gmail

        data1.save()
        return redirect('profile')
    
    return render(request,'update.html',{'data1':data1})



            


