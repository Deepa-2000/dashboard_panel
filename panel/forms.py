from django import forms
from .models import Orders
# from .models import Products

class OrdersForm(forms.ModelForm):

    class Meta:
        model= Orders
        fields= "__all__"
        widgets= {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


# class ProductsForm(forms.ModelForm):
  
#     class Meta:
#         model= Products
#         fields= "__all__"
#         widgets= {
#             'product_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'product_price': forms.TextInput(attrs={'class': 'form-control'}),
#             'quantity': forms.TextInput(attrs={'class': 'form-control'}),
#             'image':forms.ImageField(attrs={'class': 'form-control'}),
#             'description': forms.TextInput(attrs={'class': 'form-control'}),
#         }