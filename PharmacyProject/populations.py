import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fake = Faker()

def populate(N=5):

    for entry in range(N):

        fake_fname = fake.first_name()
        fake_lname = fake.last_name()
        fake_email = fake.email()

        user = User.objects.get_or_create(first_name = fake_fname, last_name = fake_lname, email = fake_email)[0]

if __name__== "__main__":

    print("is running")
    populate(20)
    print("successful")
