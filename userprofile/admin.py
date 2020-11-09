from django.contrib import admin

# Register your models here.
from userprofile.models import User

admin.site.register(User)