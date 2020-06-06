from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Instructor)
admin.site.register(Admin_Account)
admin.site.register(Device)
admin.site.register(Request)