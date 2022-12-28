from django.contrib import admin
from .models import Enquire


class EnquireAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

admin.site.register(Enquire, EnquireAdmin)
