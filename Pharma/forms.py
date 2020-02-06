from django import forms
from Pharma.models import Medicine, Transactions

class MedicineForm(forms.ModelForm):
    class Meta():
        model = Medicine
        fields = '__all__'


class TransactionsForm(forms.ModelForm):
    class Meta():
        model = Transactions
        fields = '__all__'
