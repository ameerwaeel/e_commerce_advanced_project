from django.shortcuts import render ,redirect
from . models import *
from . forms import *
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_loin
from django .contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
 # fields = ['first_name','last_name','phone_number','email','country'] this filed in form to use in cleaned_data
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            country=form.cleaned_data['country']
            phone_number=form.cleaned_data['phone_number']
            password=form.cleaned_data['password']
            username=email.split('@')[0] # to create username from email it will taked from email
# def create_user(self,first_name,last_name,username,email,country,password=None): this filed in models in creat_user fun to use in user
                                        #    form=class model of fun (create_user)
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,country=country,password=password,username=username)
            user.phone_number=phone_number
            user.save()

            # user activate
            doman_name=get_current_site(request)   # to get domain in email like this www.ameerdjangosite.com
            mail_subject='please,active your account !' # the title of message in email
            message=render_to_string('account_verification_email.html',{
                'user':user,
                'domain':doman_name,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),

                },)  # message 
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            return redirect('login' + f'?command=verfication&mail={email}')
    else:
        form=RegisterForm()

    context={
        'form':form,

    }        
    return render(request,'register.html',context)

def login(request):
    if request.method== 'POST':
        email = request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(email=email,password=password)
        if user is not None:
            if user.is_active:
                auth_loin(request,user)
                messages.success(request,'login is successfuly.')
                return redirect('store:home')
            else:
                messages.error(request,' your accounts is not active.')

        else:
            messages.error(request,' invalied login is not successfuly.')

            return redirect('accounts:login')   
    return render(request,'login.html')


def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,'your account is activate.')
        return redirect('accounts:login')
    else:
        messages.error(request,'your account is not activate,please try again .')
        return redirect('accounts:register')

