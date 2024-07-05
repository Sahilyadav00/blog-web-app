from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from passlib.hash import pbkdf2_sha256 as sha
from .models import AddUser
from django.core.mail import send_mail
from random import randint

from blogdata.form import Blog




#def hello(request):
#    return HttpResponse("This is blog page")
#def login(request, name):
#    return HttpResponse(f"WELCOME: {name}")
#def details(request, name, age, city):
#    return HttpResponse(f"WELCOME: {name} - {age} - {city}")

def index(request):
    if request.session.get('islogin'):
        return render(request, 'afterlogin.html')
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def login(request):
    if request.session.get('islogin'):
        return render(request, 'afterlogin.html')
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def password_validation(password: str):
    if len(password) >= 8:
        lower = 0
        upper = 0
        number = 0
        special = 0
        for i in password:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isnumeric():
                number += 1
            elif i in "!@#$%^&*":
                special += 1

        if lower >= 1 and upper >= 1 and number >= 1 and special >= 1:
            return True

    return False 


class AfterSignup(View):

    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        enc_pass = sha.hash(password)

        try:
            AddUser.objects.get(email=email)

        except:
            if password_validation(password):
                otp = randint(1000, 9999)
                request.session['otp'] = str(otp)
                request.session['name'] = name
                request.session['phone'] = phone
                request.session['email'] = email
                request.session['password'] = enc_pass

                send_mail(
                            "Email Verification For Bloscot",
                            f"OTP for verification is {otp}",
                            "m75116516@gmail.com",
                            [email],
                            fail_silently=False,
                        )
                msg = "Please check your mail for otp"

                return render(request, 'otp.html', {'msg':msg})
            
            else:
                msg = """Invalid Password please follow password condition
                         password contain at least 8 charcters
                         One Upper case charcter(A)
                         One lower case charcter(a)
                         One number case charcter(1)
                         One special case charcter(@)"""
                
                return render(request, 'signup.html', {'msg': msg})
            
        else:
            msg = "User Already Registered"
            return render(request, 'login.html',{'msg':msg})


class AfterLogin(View):

    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        passd = request.POST.get('password')

        try:
            obj = AddUser.objects.get(email=email)
        
        except:
            msg = "User Not Fount"
            return render(request, 'login.html', {'msg':msg})
        
        else:
            if sha.verify(passd, obj.password):
                request.session['email'] = email
                request.session['islogin'] = 'true'
                return render(request, 'afterlogin.html')
            
            else:
                msg = "Incorrect Password"
                return render(request, 'login.html', {'msg':msg})
            

class Checkotp(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):

        otp1 = request.POST.get('otp')
        otp2 = request.session['otp']
        if otp1 == otp2:
            name = request.session['name']
            phone = request.session['phone']
            email = request.session['email']
            enc_pass = request.session['password']

            AddUser.objects.create(name=name, phone=phone, email=email, password=enc_pass)

            del request.session['otp']
            del request.session['name']
            del request.session['phone']
            del request.session['email']
            del request.session['password']

            msg = "User Successfully Registered"
            return render(request, 'login.html',{'msg':msg})
        
        else:
            msg = 'Invalid otp'
            return render(request, 'signup.html', {'msg':msg})
        

def logout(request):

    del request.session['email']
    del request.session['islogin']

    return render(request, 'login.html')


def addblog(request):

    form = Blog()

    return render(request, 'blogform.html', {'form':form})





















        # return HttpResponse(f"""
        #                         NAME     : {name} 
        #                         PHONE    : {phone} 
        #                         EMAIL    : {email} 
        #                         PASSWORD : {password}
        #                     """)

