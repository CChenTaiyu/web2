from django.contrib import admin


# Register your models here.
from .models import user, consumption_record
admin.site.register(user)
admin.site.register(consumption_record)