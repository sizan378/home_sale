import random 
import string 

from autoslug import AutoSlugField
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.common.models import TimeStampedUUIDModel


User = get_user_model()

class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return super(PropertyPublishedManager, self).get_queryset().filter(published_status=True)



class Property(TimeStampedUUIDModel):
    class AdvertType(models.TextChoices):
        FOR_SALE = "For Sale",_("For Sale")
        FOR_RENT = "For rent",_("For rent")
        AUCTION = "Auction", _("Auction")

    class PropertyType(models.TextChoices):
        HOUSE = "House",_("House")
        APARTMENT = "Appointment", _("Appointment")
        OFFICE = "Office", _("Office")
        WAREHOUSE = "Warehouse", _("Warehouse")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(User,verbose_name=_("Agent,Seller or Buyer"), related_name="agent_buyer", on_delete=models.DO_NOTHING)
    title = models.CharField(_("Title"), max_length=200, blank=True)
    slug = AutoSlugField(populate_from="title", unique=True, max_length=255)
    ref_code = models.CharField(_("Ref Code"), max_length=255, unique=True, blank=True,)
    description = models.TextField(_("Description"), blank=True)
    country = CountryField(_("Country"), blank=True)
    city = models.CharField(_("City"), max_length=100)
    postal_code = models.CharField(_("Postal Code"), max_length=50)
    street_address = models.CharField(_("Street Address"), max_length=150)
    property_number = models.IntegerField(_("Property Number"))
    price = models.DecimalField(verbose_name=_("Price"), decimal_places=2, max_digits=8)
    tax = models.DecimalField(_("Tax"), decimal_places=2, max_digits=6)
    plot_area = models.DecimalField(_("Plot Area"), decimal_places=2, max_digits=8)
    total_floors = models.IntegerField(_("Total Floors"))
    bedrooms = models.IntegerField(_("BEDrooms"))
    bathrooms = models.DecimalField(_("Bathrooms"), decimal_places=2, max_digits=8)
    advert_type = models.CharField(_("Advert Type"), max_length=50, choices=AdvertType.choices)
    property_type = models.CharField(_("Property Type"), max_length=50, choices=PropertyType.choices)
    cover_photo = models.ImageField(_("Cover Photo"), null=True, blank=True)
    photo1 = models.ImageField(_("photo1"), null=True, blank=True)
    photo2 = models.ImageField(_("photo2"), null=True, blank=True)
    photo3 = models.ImageField(_("photo3"), null=True, blank=True)
    photo4 = models.ImageField(_("photo4"), null=True, blank=True)
    published_status = models.BooleanField(_("published_status"), default=False)
    views = models.IntegerField(_("Total views"), default=0)
    objects = models.Manager()
    published = PropertyPublishedManager()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.description(self.description)
        self.ref_code = "".join(random.choice(string.ascii_uppercase + string.digits, k=10))
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        tax_percentage = self.tax
        property_price = self.price 
        tax_amount = round(tax_percentage * property_price, 2)
        price_after_tax = float(round(property_price + tax_amount, 2))
        return price_after_tax


class PropertyView(TimeStampedUUIDModel):
    ip = models.CharField(_("ip address"), max_length=200)
    property = models.ForeignKey(Property, related_name="properties_views", on_delete=models.CASCADE)


    def __str__(self):
        return (
            f"Total views on - {self.property.title} is - {self.property.views} views"
        )

    class Meta:
        verbose_name = _("Total Property View")
        verbose_name_plural = _("Total Property Views")
    