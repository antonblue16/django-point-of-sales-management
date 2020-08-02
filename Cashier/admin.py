from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.InPos)
admin.site.register(models.OutPos)
admin.site.register(models.CashierPos)