from django.contrib import admin

from apps.models import Packages


# Register your models here.
@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    pass
