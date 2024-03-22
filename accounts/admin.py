from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts import models, forms

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", )}), )
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name", )}), )
    
admin.site.register(models.CustomUser, CustomUserAdmin)