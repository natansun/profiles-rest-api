from django.contrib import admin
from profiles_api import models

# Register your models here.

# register the user profile to admin site
admin.site.register(models.UserProfile)
