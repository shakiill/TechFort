from django.contrib import admin

# Register your models here.
# email: demo@gmail.com pass: demo
from apps.account.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)
# Register your models here.
