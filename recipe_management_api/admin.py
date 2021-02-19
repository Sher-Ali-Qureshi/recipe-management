from django.contrib import admin

from recipe_management_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.UserRecipe)