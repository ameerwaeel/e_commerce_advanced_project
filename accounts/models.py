from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
import pycountry
# Create your models here.



class MyAcountManger(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,country,password=None):
        if not email:
            raise ValueError('you must have an email')
        if not username:
            raise ValueError('you must have an username')
        user=self.model(
            email=self.normalize_email(email),#normalize_email to remove email as captel letters
            first_name=first_name,
            last_name=last_name,
            username=username,
            country=country,

        )
        user.set_password(password)#to hashcoding for password
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,password=None,**extra_fields):
        user=self.create_user(
            email=self.normalize_email(email),#normalize_email to remove email as captel letters
            first_name=first_name,
            last_name=last_name,
            username=username,
            country=extra_fields.get('country', 'us'),  # Default country if not provided

        )
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
 

class Account(AbstractBaseUser):
    @staticmethod
    def get_country():
        countries=list(pycountry.countries)
        contry_chooices=[(country.alpha_2,country.name) for country in countries ]
        return contry_chooices
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    country=models.CharField(max_length=2,choices=get_country(),default='us')
    phone_number=models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)  # Updates on each login
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)


    USERNAME_FIELD='email'# to login with your email not username
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'country']
    objects=MyAcountManger()# مدير او اساسي علي كلاس اكونت  MyAcountManger  من الاخر عشان تخلي كلاس 
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):#to give permissions
        return self.is_admin
    def has_module_perm(self,app_label):#to apper all apps
        return True
    def has_module_perms(self, app_label):
        """
            Return True if the user has permissions to view the app `app_label`.
        """
        return True