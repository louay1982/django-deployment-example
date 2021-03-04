import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'third.settings')

import django
django.setup()

from appthree.models import User
from faker import Faker

Fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        fake_name=Fakegen.name().split()
        fake_firstname=fake_name[0]
        fake_lastname=fake_name[1]
        fake_email=Fakegen.email()

        user = User.objects.get_or_create(firstname=fake_firstname,
                                          lastname=fake_lastname,
                                          email=fake_email)[0]
if __name__=='__main__':
    print("populating databases")
    populate(20)
    print("complete")
