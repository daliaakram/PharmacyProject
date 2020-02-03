from django.db import models

# Create your models here.


class Medicine(models.Model):
    scientific_name = models.TextField(max_length=264)
    trade_name = models.TextField(max_length=264)
    alternate1 = models.TextField(max_length=264)
    alternate2 = models.TextField(max_length=264)
    qnt = models.PositiveIntegerField()
    item_price = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.trade_name


class Transactions(models.Model):
    med_name = models.ForeignKey('Medicine', on_delete = models.CASCADE)
    sell_qnt = models.PositiveIntegerField()
    sell_price = models.PositiveIntegerField()
    sell_date = models.DateTimeField()

    def __str__(self):
        return self.med_name.trade_name
