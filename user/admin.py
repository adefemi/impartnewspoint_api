from django.contrib import admin
from .models import GenericFileUpload, Marketting, MarkettingBanners

# Register your models here.
admin.site.register((GenericFileUpload, MarkettingBanners, Marketting))
