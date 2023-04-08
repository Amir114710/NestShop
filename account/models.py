from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='پست الکترونیک',
        max_length=255,
    )
    username = models.CharField(max_length=200, verbose_name='نام کاربری' ,unique=True , null=True, blank=True)
    phone = models.CharField(max_length=12 , verbose_name='شماره تلفن', default='0' ,unique=True,)
    image = models.ImageField(upload_to='UserImage' , verbose_name='عکس کاربر' , null=True, blank=True)
    Full_name = models.CharField(max_length=200 , verbose_name='نام کامل' , null=True, blank=True)
    is_Accept_terms = models.BooleanField(default=False , verbose_name='پذیرفتن شرایط')
    is_active = models.BooleanField(default=True , verbose_name='فعال')
    is_admin = models.BooleanField(default=False , verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural ='کاربر ها'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class OTP(models.Model):
    token = models.CharField(max_length=12 , null=True)
    phone = models.CharField(max_length=12)
    is_Accept_terms = models.BooleanField(default=False , verbose_name='پذیرفتن شرایط')
    code = models.SmallIntegerField(null=True, blank=True)
    expiration_date =  models.DateTimeField(null=True, blank=True , auto_now_add=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "کد:otp"
        verbose_name_plural = "کد:otp ها"

class Address(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='addresses')
    fullname = models.CharField(max_length=100)
    address = models.TextField(null=True , blank=True , verbose_name='ادرس')
    email = models.EmailField(null=True , blank=True , verbose_name='ایمیل')
    phone = models.CharField(max_length=12 , verbose_name='تلفن')
    postal_code = models.CharField(max_length=10)


    def __str__(self) -> str:
        return self.user.phone
    
    class Meta:
        verbose_name = "ادرس"
        verbose_name_plural = "تنظیمات قسمت ادرس"
