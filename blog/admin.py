from django.contrib import admin
from .models import AddUser
from .models import Addblog

# Register your models here.

admin.site.register(AddUser)

admin.site.register(Addblog)
