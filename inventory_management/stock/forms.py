from django import forms
from .models import StockTransaction


class StockTransactionForm(forms.ModelForm):

    class Meta:

        model = StockTransaction

        fields = [
            'product',
            'transaction_type',
            'quantity',
            'remarks'
        ]