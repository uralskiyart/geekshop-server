from django.core.management import BaseCommand

from users.models import User, ExtendUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.all():
            ExtendUser.objects.create(user=user)