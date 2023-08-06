from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Userform,Loginform
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Answer,Question,Attemtnumber,Category
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def studentsignup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm=Userform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Your account is created successfully')
                return redirect('studentlogin')

        else:
            fm=Userform()
        return render(request,'studentsignup.html',{'u':fm})
    else:
        return redirect('quizhome')



def studentlogin(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            a=Loginform(request=request,data=request.POST)
            if a.is_valid():
                username=a.cleaned_data['username']
                password=a.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('quizhome')
        else:
            a=Loginform(request)
        return render(request,'studentlogin.html',{'u':a})
    else:
        return redirect('quizhome')
    

@login_required()
def studentlogout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='studentlogin')
def quizhome(request):
    if request.method == 'POST':

        
        question=0
        marks=0
        totalq=0
        q=[]
       
        for x,y in request.POST.items():
            a=Answer.objects.only('question','answer').filter(question__question=x,answer=y)
            b=Answer.objects.only('question').filter(question__question__exact=x).count()
            c=Answer.objects.only('marks','question').filter(question__question=x,answer=y).values('marks')
            for sub in c:
                
                    sub['marks'] = int(sub['marks'])
                    
                    if a:
                        marks+=sub['marks']
                    
                    
                    if b:
                        question+=1
                    totalq+=1
            
                    c=Answer.objects.select_related('question').filter(question__question=x).values('category__cname')

                    for z in c:
                        q+=[z['category__cname']]

                
        listToStr = ','.join([str(elem) for elem in q])
        attempt=Attemtnumber.objects.filter(student=request.user.id).values("noattempt").count()
        b=Attemtnumber()
        b.marks=marks
        b.toatalquestion=totalq-1
        b.noattempt=attempt+1
        b.student=User.objects.get(id=request.user.id)
        b.totalattemptquestion=question
        b.category=listToStr
        b.save()
        return redirect(reverse('result'))
    else:
        a=Answer.objects.select_related('question').all()
        b=Answer.objects.select_related('question').count()
        
    return render(request,'quizhome4.html',{'a':a,'b':b})


@login_required(login_url='studentlogin')
def result(request):
    res=Attemtnumber.objects.filter(student=request.user.id).all().last()
    return render(request,'result.html',{'res':res})

@login_required(login_url='studentlogin')
def cate(request,slug):
    c=Category.objects.filter(cname=slug)
    return render(request,'cat.html',{'c':c})
