from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Post


class Command(BaseCommand):
    help = "Adds posts to the database"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(10000):
            Post.objects.create(title=fake.name(), body=fake.text())

        print("Completed!!! Check your database.")
