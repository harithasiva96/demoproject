from django.shortcuts import render,redirect
from django.http import HttpResponse
from mydemoapp.models import registration
from mydemoapp.models import add_teacherinfo
from mydemoapp.models import files
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout


# Create your views here.
def home(request):
         return render(request,template_name='home.html')

def home2(request):
    if request.method=='POST':
        a=request.POST['first_name']
        b=request.POST['last_name']
        c=request.POST['age']
        d=request.POST['phone']
        e=request.POST['email']
        f=request.POST['username']
        g= request.POST['password']
        h=registration(first_name=a, last_name=b, age=c, phone=d, email=e, username=f, password=g )
        h.save()
        h1=User(first_name=a, last_name=b, email=e, username=f)
        h1.set_password(g)
        h1.save()
        return HttpResponse('<script>alert("data saved successfully"),windows.location="/login";</script>')
    return render(request,template_name='form.html')

def admin_home(request):
    return render(request,template_name='admin_home.html')

def login(request):
    if request.method=="POST":
        x=request.POST['username']
        y=request.POST['password']
        au=authenticate(username=x,password=y)
        print(au)
        request.session['member_id']=x
        if au is not None and au.is_superuser==1:
            # return redirect(admin_home)
            return render(request, template_name='admin_home.html')
        else:
            z=registration.objects.get(username=x)
            if z.password==y:
                if au is not None and au.is_superuser==0:
                    return render(request,template_name='user_home.html')
    return render(request,template_name='login.html')

def user_home(request):
    return render(request,template_name='user_home.html')

def edit(request):
    user_id=request.session['member_id']
    o=registration.objects.get(username=user_id)
    o1=User.objects.get(username=user_id)
    if request.method=='POST':
        o.first_name=request.POST['first_name']
        o.last_name=request.POST['last_name']
        o.age=request.POST['age']
        o.phone=request.POST['phone']
        o.email=request.POST['email']
        o.username= request.POST['username']
        o.password= request.POST['password']
        o.save()
        o1.first_name=request.POST['first_name']
        o1.last_name=request.POST['last_name']
        o1.email=request.POST['email']
        o1.save()
        return HttpResponse('<script>alert("Profile updated"),window.location="/userhome";</script>')
    return render(request,template_name='edit.html',context={'u':o})

def log_out(request):
    logout(request)
    return redirect(home)

def addinfo(request):
    if request.method=="POST":
        p=request.POST['first_name']
        q=request.POST['last_name']
        r=request.FILES['profile_pic']
        s=request.POST['email']
        t=request.POST['phone']
        v=request.POST['room_number']
        w1=request.POST['subject1']
        w2=request.POST['subject2']
        w3=request.POST['subject3']
        w4=request.POST['subject4']
        w5=request.POST['subject5']
        x=add_teacherinfo(first_name=p, last_name=q,profile_pic=r, email=s, phone=t, room_number=v, subject1=w1, subject2=w2, subject3=w3, subject4=w4, subject5=w5  )
        x.save()
        return HttpResponse('<script>alert("Saved Successfully"),window.location="/view";</script>')
    return render(request,template_name='add_teacherinfo.html')

def admin_view(request):
    k=add_teacherinfo.objects.all()
    return render(request,template_name='view.html',context={'k1':k})

def update_info(request,id):
    p_id=id
    q=add_teacherinfo.objects.get(id=p_id)
    if request.method=="POST":
        q.first_name=request.POST['first_name']
        q.last_name=request.POST['last_name']
        q.profile_pic=request.FILES['profile_pic']
        q.email=request.POST['email']
        q.phone=request.POST['phone']
        q.room_number=request.POST['room_number']
        q.subject1=request.POST['subject1']
        q.subject2=request.POST['subject2']
        q.subject3=request.POST['subject3']
        q.subject4=request.POST['subject4']
        q.subject5=request.POST['subject5']
        q.save()
        return HttpResponse('<script>alert("Updated Successfully"),window.location="/view";</script>')
    return render(request,template_name='view.html',context={'p':q})

def deletion(request,id1):
    pid=id1
    q=add_teacherinfo.objects.get(id=pid)
    q.delete()
    return HttpResponse('<script>alert("Deleted Successfully"),window.location="/view";</script>')

def user_view(request):
    k=add_teacherinfo.objects.all()
    return render(request,template_name='user_view.html',context={'k1':k})

def file_upload(request):
    if request.method == "POST":
        m=request.FILES['zip_file']
        n=request.FILES['info_file']
        n1=files(zip_file=m, info_file=n )
        n1.save()
        return HttpResponse('<script>alert("Saved Successfully"),window.location="/adminhome";</script>')
    return render(request,template_name='file.html')

def view_files(request):
    q=files.objects.all()
    return render(request,template_name='view_files.html',context={'q1':q})


