from django import forms
from Cashier.models import CashierPos, InPos, OutPos

class CashierPosForms(forms.ModelForm):

    class Meta():
        model = CashierPos
        fields = ['created_date']

        widgets = {
            'created_date':forms.DateInput(format='%d/%m/%Y')
        }

class InPosForms(forms.ModelForm):

    class Meta():
        model = InPos
        fields = ['name', 'quantity', 'unitPrice', 'price']

        