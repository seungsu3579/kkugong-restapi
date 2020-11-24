import json
from django.core.management.base import BaseCommand
from cody.models import Cody
from config import settings
import socket
import boto3


class Command(BaseCommand):

    help = "Add cody to Database"

    def handle(self, *args, **options):

        ###### s3 ######
        AWS_ACCESS_KEY_ID = "AKIAT2WNRTLX4AWNEVOK"
        AWS_SECRET_ACCESS_KEY = "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"
        AWS_REGION = "ap-northeast-2"

        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION,
        )

        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION,
        )

        bucket = session.resource("s3").Bucket(name="dressroom-base-data")

        for TARGET_PREFIX in ["cody/top", "cody/pants", "cody/shoes"]:

            for obj in bucket.object_versions.filter(Prefix=TARGET_PREFIX).all():
                key = obj.Object()._key
                cody_id = key[key.find("_") + 1 : key.find("_", key.find("_") + 1)]

                cody = Cody.objects.filter(id=cody_id)

                if len(cody) == 0:
                    cody = Cody.objects.create(
                        id=cody_id, img=f"cody/cody/cody_{cody_id}.jpg", jjim=False,
                    )
                else:
                    cody = cody[0]

                if TARGET_PREFIX == "cody/top":
                    cody.cody_top_img = key
                    cody.form += 4
                    print(f"{cody_id} top add!")
                elif TARGET_PREFIX == "cody/pants":
                    cody.cody_pants_img = key
                    cody.form += 2
                    print(f"{cody_id} pants add!")
                elif TARGET_PREFIX == "cody/shoes":
                    cody.cody_shoes_img = key
                    cody.form += 1
                    print(f"{cody_id} shoes add!")
                cody.save()

        self.stdout.write(self.style.SUCCESS(f"All cody is added to Database!"))

