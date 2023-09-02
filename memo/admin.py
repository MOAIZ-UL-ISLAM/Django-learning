from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','gender','age','occupation')
    list_display_links=('name','age')

admin.site.register(Profile)
admin.site.register(Caste)
admin.site.register(Hobby)
admin.site.register(FatherProfile)
admin.site.register(Sect)
admin.site.register(Religion)