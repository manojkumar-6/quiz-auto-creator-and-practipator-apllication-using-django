from django.http import HttpResponse
import re
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from .forms import rw
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
m=0
counts=0
def home(request):
    return render(request,"a.html")
def reg(request):
    d=rw()
    if request.method=="POST":
        t=request.POST["name"]
        y=request.POST["email"]
        u=request.POST["password"]
        q=User.objects.create_user(username=t,email=y,password=u)
        q.save()
        return redirect("accounts/login")
    return render(request,"b.html",{"d":d})
def homes(request):
    aq=key.objects.all()
    az=score.objects.all().values_list()
    az=list(az)
    print(az)
    xq=[]
    kel=[]
    cor=[]
    kl=[]
    for i in az:
        if request.user.username in i:
            print("d,j")
            xq.append(i[0])
            kel.append(i[3])
            cor.append(i[1])
    for i in az:
        qa=i[1]
        i=list(i)
        i.pop(0)
        i.insert(0,qa)
        print(i)
        kl.append(i)
    kl.sort()
    print(kl)
    print(az)
    mnb=3
    if len(kl)<=mnb:
        mnb=len(kl)
    for i in range(0,len(kl)):
        xq.append(kl[i][2])
    print(aq)
    f=list(aq)
    print(f)
    print(kel)
    return render(request,"c.html",{"f":f,"xq":xq,"kel":kel})
def create(request):
    h=k()
    if request.method=="POST":
        g=request.POST["ke"]
        #l=request.POST["j"]
        print(g)
        o=key.objects.all().values_list()
        r=list(o)
        print(r)
        for i in r:
            if g in i:
                o=1
            else:
                o=0
        print(o)
        if o:
            return redirect("create")
        else:
            u=key(ke=g,j=request.user.username)
            u.save()
            print("data saved")
            return redirect("t", g=g)

    return render(request,"d.html",{"h":h})
def t(request,g):
    print(g)
    w=questions.objects.filter(key=g)
    print(w)
    n=quest()
    if request.method=="POST":
        a=request.POST["question"]
        s=request.POST["question1"]
        d=request.POST["question2"]
        f=request.POST["question3"]
        gn=request.POST["question4"]
        h=request.POST["answer"]
        z=questions(question=a,question1=s,question2=d,question3=f,question4=gn,answer=h,key=g)
        z.save()
        return redirect("t", g=g)
    return render(request,"e.html",{'n':n,"w":w,"g":g})
def update(request,g,pk):
    f=questions.objects.filter(id=pk).first()
    print(f)
    o=quest(instance=f)
    if request.method=="POST":
        a=request.POST["question"]
        s=request.POST["question1"]
        d=request.POST["question2"]
        f=request.POST["question3"]
        gn=request.POST["question4"]
        h=request.POST["answer"]
        questions.objects.filter(id=pk).update(question=a,question1=s,question2=d,question3=f,question4=gn,answer=h,key=g)
        return redirect("t", g=g)
    return render(request,"t.html",{"form":o,"g":g})
def dele(request,g,pk):
    f=questions.objects.filter(id=pk)
    f.delete()
    return redirect("t",g=g)
def delete(request,p):
    print(p)
    f=key.objects.filter(id=p)
    g=questions.objects.all().values_list()
    print(g)
    print(f)
    f.delete()
    print("deleted")
    g=questions.objects.all().values_list()
    print(g)
    l=[]
    for i in g:
        w=i[len(l)-1]
        print(w)
        s=i[0]
        if w==p:
            r=questions.objects.filter(pk=s)
            print(r)
            r.delete()
    return redirect("homes")
def r(request):
    return redirect("/homes")
def par(request):
    if request.method=="POST":
        g=request.POST["ke"]
        #l=request.POST["j"]
        print(g)
        o=key.objects.all().values_list()
        r=list(o)
        print(r)
        for i in r:
            if g in i:
                o=1
            else:
                o=0
        print(o)
        if o:
            return redirect("quiz", g=g)
        else:
            return redirect("par")

    return render(request,"z.html")

def quiz(request,g):
    l=[]
    print("inquiz")
    global m
    global counts
    print(m,counts)
    f=questions.objects.all().values_list()
    print(f)
    c=[]
    for i in f:
        if g in i:
            c.append(i[0])
    print(c)
    for i in f:
        if g in i and len(c)-1>=m:
            s=questions.objects.filter(id=c[m])
            qw=s.values_list()
            #print(qw[0])
            acd=qw[0][6]
            m+=1
            return render(request,"y.html",{"s":qw[0][1],"d":qw[0][2],"l":qw[0][3],"k":qw[0][4],"j":qw[0][5],"g":g,"acd":acd})

    print(m,counts)
    das=score(se=counts,name=request.user.username,participated=g)
    das.save()
    print(das)
    print("quiz completed")
    m=0
    counts=0
    print(m,counts)
    return HttpResponse("quizcompleted")
def analyse(request,g,acd):
    global counts
    if request.method=="POST":
                xc=request.POST["name"]
                if xc==acd:
                    counts+=1
                    print("counts"+str(counts))
                return redirect(quiz, g=g)

def u(request,i):
    qa=key.objects.filter(id=i).values_list()
    pr=(qa[0][1])
    h=questions.objects.all().values_list()
    l=[]
    for s in h:
        if pr in s:
            s="question  :"+s[1]+'  =======  '+"option1    :"+s[2]+"   =====   "+"option2    :"+s[3]+'   ====    '+"option3     :"+s[4]+"option4     :"+s[5]+'   ====   '+"answer     :"+s[6]
            l.append(s)
    return render(request,"q.html",{"f":l})
def sees(request,xq):
    print(xq)
    xq=xq[1:len(xq)-1]
    xq=xq.split(",")
    print(xq[0])
    if len(xq)<5:
        g="there are no enough participants to dispaly leader board"
    else:
        g="the first position is by"+str(xq[len(xq)-1])+"the second position is "+str(xq[len(xq)-2])+"the last position is"+str(xq[len(xq)-3])

    return render(request,"x.html",{"a":xq[0],"s":xq[len(xq)-1],"g":g})







