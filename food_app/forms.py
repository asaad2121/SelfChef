from django import forms
from food_app.models import Recipes, UserData

class UserForm(forms.ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = UserData
        fields = '__all__'
        widgets={
            'user_name' : forms.TextInput(attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
                }),
            'user_email' : forms.EmailInput(attrs={
                'placeholder': 'User Email',
                'class': 'form-control'
                }),
            'user_password' : forms.PasswordInput(attrs={
                'placeholder': 'User Email',
                'class': 'form-control'
                }),
        }

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
        widgets={
            'rname' : forms.TextInput(attrs={
                'placeholder': 'Recipe Name',
                'class': 'form-control'
                }),
            'rdescription' : forms.TextInput(attrs={
                'placeholder': 'Recipe description',
                'class': 'form-control'
                }),
            'ringredients' : forms.TextInput(attrs={
                'placeholder': 'Recipe ingredients',
                'class': 'form-control'
                }),
            'rstep1' : forms.TextInput(attrs={
                'placeholder': 'Recipe Step 1',
                'class': 'form-control'
                }),
            'rstep2' : forms.TextInput(attrs={
                'placeholder': 'Recipe Step 2',
                'class': 'form-control'
                }),
            'rstep3' : forms.TextInput(attrs={
                'placeholder': 'Recipe Step 3',
                'class': 'form-control'
                }),
            'rstep4' : forms.TextInput(attrs={
                'placeholder': 'Recipe Step 4',
                'class': 'form-control'
                }),
            'rstep5' : forms.TextInput(attrs={
                'placeholder': 'Recipe Step 5',
                'class': 'form-control'
                }),
        }