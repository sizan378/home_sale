from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel


class Enquire(TimeStampedUUIDModel):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(_('Phone Number'),max_length=11)
    email = models.EmailField(_('Email'),max_length=254)
    subject  = models.CharField(_('Subject'),max_length=100)
    message  = models.TextField(_('Message'),null=True,blank=True)

    def __str__(self):
        return self.email 

    class Meta:
            verbose_name = _('Enquire')
            verbose_name_plural = _('Enquires')
