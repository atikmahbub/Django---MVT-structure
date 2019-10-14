from .models import Product
from django import forms

class ProductForm(forms.ModelForm):

    title = forms.CharField(label='Title',widget=forms.TextInput(attrs={"placeholder":"your title"}))
    price = forms.DecimalField(initial=0.00)
    class Meta:
        model = Product
        fields = [ "title" , "description" , "summary" ,"price" ,"featured" , "image"]