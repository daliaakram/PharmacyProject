from django.db import models

# Create your models here.


class Medicine(models.Model):
    scientific_name = models.CharField(max_length=264,null=True,)
    trade_name = models.CharField(max_length=264, null=True,)
    alternate1 = models.CharField(max_length=264, null=True,)
    alternate2 = models.CharField(max_length=264, null=True,)
    qnt = models.PositiveIntegerField(null=True,)
    item_price = models.PositiveIntegerField(null=True,)
    start_date = models.DateTimeField(null=True,)
    end_date = models.DateTimeField(null=True,)

    def __str__(self):
        return self.trade_name


class Transactions(models.Model):
    med_name = models.ForeignKey('Medicine', on_delete = models.CASCADE)
    sell_qnt = models.PositiveIntegerField(null=True,)
    sell_price = models.PositiveIntegerField(null=True,)
    sell_date = models.DateTimeField(null=True,)

    def __str__(self):
        return self.med_name.trade_name
