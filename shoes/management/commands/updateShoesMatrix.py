from django.core.management.base import BaseCommand
from utils.matrix import Matrix


class Command(BaseCommand):

    help = "Update top matrix for recommand system"

    def handle(self, *args, **options):

        m = Matrix()
        m.shoesMatrixToCsv()

        self.stdout.write(self.style.SUCCESS(f"All tops are added in matrix!"))

