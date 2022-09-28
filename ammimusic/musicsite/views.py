from django.shortcuts import render, redirect
from django.http import HttpResponse
from musicsite.models import NewRegister,Mymedia
def home(request):
    data = Mymedia.objects.all()
    return render(request,'template/index.html',{"all":data})
def contact(request):
    return render(request,'template/contact.html')
def joinus(request):
    return render(request,'template/joinus.html')

def RegForm(request):
    return render(request,'template/Register.html')

def RegData(request):
    if request.method=="POST":
        a=request.POST['t1'];
        b=request.POST['t2'];
        c=request.POST['t3'];
        d=request.POST['t4'];
        e=request.POST['t5'];
        f=request.POST['t7'];
        
        print("Username:-",a)
        data=NewRegister(FirstName=a,MiddleName=b ,LastName=c,Email=d,Number=e,Password=f)
        data.save()
        msg="Data is register"
        return render(request,'template/msg.html',{"abc":msg})
    else:
        return render(request,'template/Register.html')
    
def login(request):
    return render(request,'template/login.html')
def logincode(request):
    if request.method=="POST":
        email=request.POST['t1']
        pwd=request.POST['t2']
        if email == "klalit434@gmail.com" and pwd == "Lalit":
            request.session['admin']= email
            return redirect("/admin1/")
        else:
            user = NewRegister.objects.filter(Email=email,Password=pwd).count()
            if(user==0):
                user = "Not Match"
                return render(request,"template/msg1.html",{"msg1":user})
            else:
               request.session['email'] = email
               return redirect("/user/")
def admin(request):
    if request.session.has_key('admin'):
        email = request.session['admin']
        return render(request,"template/admin.html",{"usernames" : email})
    else :
        return redirect('/login/')
def user(request):
    if request.session.has_key('email'):
        email = request.session['email']
        return render(request,"template/user.html",{"usernames" : Email})
    else :
        return redirect('/login/')
        
        
        
def logout(request):
    return render(request,'template/logout.html')
def showcategory(request):
    return render(request,'template/showcategory.html')
def showsongs (request):
    data = Mymedia.objects.all()
    return render(request,'template/showsongs.html',{"alldata":data})
def addcategory(request):
    return render(request,'template/addcategory.html')
def addsongs(request):
    return render(request,'template/addsongs.html')
    


def media(request):
    if request.method=="POST":
        a=request.POST['t1'];
        b=request.POST['t2'];
        c=request.POST['t3'];
        d=request.FILES['t4'];
        e=request.POST['t5'];
        f=request.POST['t6'];
        data=Mymedia(song=a,singer=b ,title=c,file=d,rating=e,views=f)
        data.save()
        msg="Data is register"
        return render(request,'template/msg.html',{"abc":msg})
    else:
        return render(request,'template/addsongs.html')

def showuser(request):
    data = NewRegister.objects.all()
    return render(request,'template/showuser.html',{"alldata":data})
def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    if request.session.has_key('admin'):
        del request.session['admin']
    return redirect('/login/')
 
def ushowcategory(request):
    return render(request,'template/ushowcategory.html')
def ushowsongs (request):
    data = Mymedia.objects.all()
    return render(request,'template/ushowsongs.html',{"alldata":data})
def uaddsongs(request):
    return render(request,'template/uaddsong.html')
    
def umedia(request):
    if request.method=="POST":
        a=request.POST['t1'];
        b=request.POST['t2'];
        c=request.POST['t3'];
        d=request.FILES['t4'];
        e=request.POST['t5'];
        f=request.POST['t6'];
        data=media(song=a,singer=b ,title=c,file=d,rating=e,view=f)
        data.save()
        msg="Data is register"
        return render(request,'template/msg.html',{"abc":msg})
    else:
        return render(request,'template/uaddsong.html')

    
def account(request):
    Email=request.session['email']
    data=NewRegister.objects.filter(Email=Email).all()
    return render(request, 'template/account.html',{"all":data})
def changepassword(request):
    if request.method=="POST":
        a=request.POST['t2'];
        b=request.POST['t11'];
        data=NewRegister.objects.filter(Email=b).update(Password=a)
        msg="Password Change"
        Email=request.session['email']
        data=NewRegister.objects.filter(Email=Email).all()
        return render(request,'template/msg.html',{"all":data,"abc":msg})
    else:
        return render(request,'template/Register.html')   
def user(request):
    return render(request,'template/user.html')
      
   
	
# Create your views here.
