import os
import django

from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_project.settings')
django.setup()

from quotes.models import Quote, Tag, Author # noqa

client = MongoClient('mongodb+srv://tsarevycholha:Rk3f448t5vpuTHu3@newcluster.w9thwg8.mongodb.net/?retryWrites=true&w=majority&appName=NewCluster')

db = client.hw

author = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description'],
    )
