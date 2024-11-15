from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser , Group , Permission
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
indian_phone_number_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message="Enter a valid 10-digit Indian phone Number.",
    code='invalid_phone_number'
)
class Authuser(AbstractUser) :
    phone_numbers  = models.CharField(max_length=10 ,
     null=True , 
     blank=True ,
     validators=[indian_phone_number_validator],
     help_text= "Enter a indian phone number"
    )
    date_of_birth = models.CharField(max_length=50 , null=True)
    last_login_ip = models.CharField(max_length=50 , null=True)
    groups = models.ManyToManyField(
        Group,
        related_name="my_group",  
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
    def __str__(self):
        return self.username
    


