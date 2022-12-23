from django.db import models
from django.contrib.auth import get_user_model 
from django.utils.translation import gettext_lazy as _ 
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = 'Male', _("Male")
    FEMALE = "Female", _('Female')
    OTHER = "Other", _('Other')


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(max_length=11)
    about_me = models.TextField()
    license = models.CharField(max_length=30, blank=True,null=True, unique=True)
    profile_photo = models.ImageField()
    gender = models.CharField(max_length= 20, choices=Gender.choices)
    country = CountryField(blank=True, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    is_buyer = models.BooleanField(default=False, null=True, blank=True, help_text='Are you a buyer')
    is_seller = models.BooleanField(default=False, null=True, blank=True, help_text="Are you a seller")
    is_agent = models.BooleanField(default=False, null=True, blank=True, help_text="Are you a agent")
    top_agent = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(default=0, null=True, blank=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
