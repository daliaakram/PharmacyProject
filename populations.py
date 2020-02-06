from datetime import date
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PharmacyProject.settings')

import django
django.setup()

import random
from Pharma.models import Medicine, Transactions
from faker import Faker

fake = Faker()

sc_names = ['artevirifen', 'bolipredimastat', 'calcinabitroline', 'nalapred', 'nalbulin', 'guanproget', 'artekefinermin', 'estripirox', 'guanacastat', 'pegamelteon', 'ceftinib',
            'gliracetam', 'virast', 'nifurprostsetron', 'estragrelivastatin', 'calciiergcuronium', 'arteidipine', 'gliidermin', 'nalakefiprazole','tropnabaspodar']

tr_names = ['Somanam', 'Optiferal', 'Sanctunavir', 'Azelavene', 'Alomin', 'Cromectin', 'Enzavene', 'Docpirox', 'Acanstrin', 'Calcidipine', 'Cefostadil', 'Atranitor', 'Dexatalol', 'Ribanuvia',
            'Bactesetron', 'Testodafinil', 'Fosinoprine', 'Cypropatch', 'Augmentisol', 'Albutegen']

# def add_scname():
#     s = Medicine.objects.get_or_create(scientific_name=random.choice(sc_names))[0]
#     s.save()
#     return s
#
# def add_trname():
#     t = Medicine.objects.get_or_create(trade_name=random.choice(tr_names))[0]
#     t.save()
#     return t


def populate(N=5):

    for entry in range(N):

        fake_sname = sc_names[entry]
        fake_tname = tr_names[entry]
        fake_alt1 = tr_names[N-entry-1]
        fake_alt2 = sc_names[N-entry-1]
        fake_qnt = fake.random_int(10, 100)
        fake_price = fake.random_int(20, 200)
        fake_sdate = date.today()
        fake_edate = date.today()
        fake_sellqnt = fake.random_int(10, 100)
        fake_sellprice = fake.random_int(30, 50)
        fake_selldate = date.today()


        med = Medicine.objects.get_or_create(scientific_name = fake_sname, trade_name = fake_tname, qnt = fake_qnt, item_price = fake_price, start_date = fake_sdate, end_date = fake_edate)[0]

        trans = Transactions.objects.get_or_create(med_name = med, sell_qnt = fake_sellqnt, sell_price = fake_sellprice, sell_date = fake_selldate)[0]

if __name__== "__main__":

    print("is running")
    populate(20)
    print("successful")
