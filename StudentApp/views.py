from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from StudentApp.models import City, Course, Student2


# Create your views here.
@login_required
@never_cache
def insert_fun(request):
    if request.method == 'POST':
        s1=Student2()
        s1.Stud_name = request.POST['txtName']
        s1.Stud_phno = int(request.POST['txtPhno'])
        s1.Stud_email = request.POST['txtEmail']
        s1.Stud_fees = int(request.POST['txtFees'])
        s1.Stud_course=Course.objects.get(course_name=request.POST['ddlCourse'])
        s1.Stud_city=City.objects.get(city_name=request.POST['ddlCity'])
        s1.save()
        return redirect('insert')

    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request,'insert_student.html',{'CityData':city,'CourseData':course})

@login_required
@never_cache
def display_fun(request):
    s1 = Student2.objects.all()
    return render(request,'display_student.html',{'data':s1})

@login_required
@never_cache
def update_fun(request,id):
    s1=Student2.objects.get(id = id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.Stud_name = request.POST['txtName']
        s1.Stud_phno = int(request.POST['txtPhno'])
        s1.Stud_email = request.POST['txtEmail']
        s1.Stud_fees = int(request.POST['txtFees'])
        s1.Stud_course = Course.objects.get(course_name=request.POST['ddlCourse'])
        s1.Stud_city = City.objects.get(city_name=request.POST['ddlCity'])
        s1.save()
        return redirect('display')
    else:
        return render(request,'update_student.html',
                      {'data':s1,
                       'CityData':city,
                       'CourseData':course
                       })

@login_required
@never_cache
def delete_fun(request,id):
    s1=Student2.objects.get(id = id)
    s1.delete()
    return redirect('display')


def login_fun(request):
    if request.method=='POST':
        u_name = request.POST['txtUsername']
        u_pswd = request.POST['txtUserPassword']
        user = authenticate(username=u_name,password=u_pswd)
        if user is not None :
            if user.is_superuser:
                login(request,user)
                request.session['Name'] = u_name
                return redirect('home')
        else:
            return render(request,'login.html',
                           {'msg':'enter proper username & password'})
    return render(request,'login.html',{'msg':''})


def reg_fun(request):
    if request.method=='POST':
        u_name = request.POST['txtName']
        u_password = request.POST['txtPswd']
        u_email = request.POST['txtEmail']

        u2= User.objects.filter(Q(username=u_name),Q(email=u_email)).exists()
        if u2:
            return render(request,'register.html',{'msg':'enter proper username and email'})
        else:
            u1 = User.objects.create_superuser(username=u_name,password=u_password,email=u_email)
            u1.save()
            return redirect('log')
    else:
        return render(request,'register.html',{'msg':''})



@login_required
@never_cache
def home_fun(request):
    return render(request,'home.html',{'data':request.session['Name']})


def logout_fun(request):
    logout(request)
    return redirect('log')