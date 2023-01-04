from django import forms
from food_app.models import Recipes

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