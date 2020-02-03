from django.contrib import admin
from Pharma.models import Medicine, Transactions
# Register your models here.


class ListMedicine(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['scientific_name', 'trade_name', 'qnt', 'item_price']

class ListTransactions(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['med_name', 'sell_qnt', 'sell_price']

admin.site.register(Medicine, ListMedicine)
admin.site.register(Transactions, ListTransactions)
