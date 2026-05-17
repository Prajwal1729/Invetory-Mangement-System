from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'product_name',
            'product_sku',
            'product_image',
            'description',
            'category',
            'supplier',
            'price',
            'quantity',
            'minimum_stock_level',
            'barcode',
            'product_status'
        ]

        widgets = {

            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),

            'product_status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({
                'class': 'form-control'
            })