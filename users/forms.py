from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Profil

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': "Ism", 
            'last_name': "Sharif", 
            'email': "Elektron manzil", 
            'username': "Login",
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})
            
            
class CustomProfileCreationForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['name' ,    'email' ,    'info' ,    'location' ,    'bio' ,    'sacial_github' ,    'sacial_linkedin'  ,    'sacial_youtube' ,    'sacial_instagram' ,    'image' ]
        
        
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})
            
            