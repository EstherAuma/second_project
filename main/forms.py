from django import forms
from .models import Branch,CountryOfOrigin,Category,Product,Sale,User
from django.contrib.auth.forms import UserCreationForm

class BranchCreationForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'


class CountryOfOriginCreationForm(forms.ModelForm):
    class Meta:
        model = CountryOfOrigin
        fields = '__all__'

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SaleCreationForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number','nationality']




