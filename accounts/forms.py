from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = UserCreationForm.Meta.fields + ("name", )
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CustomUser
        fields = UserChangeForm.Meta.fields