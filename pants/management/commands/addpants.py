import json
from django.core.management.base import BaseCommand
from pants.models import Pants, PantsImage
from config import settings
import socket
import boto3


class Command(BaseCommand):

    help = "Add json data to Database"

    def add_arguments(self, parser):
        parser.add_argument("--filename", help="json file to add")

    def handle(self, *args, **options):
        file = options.get("filename")
        MEDIA_DIR = settings.MEDIA_ROOT

        #### socket ####
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(
            (settings.PANTS_VECTORIZATION_HOST, settings.PANTS_VECTORIZATION_PORT)
        )
        ################

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
        ################

        with open(file, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        for j in json_data:
            id = list(j.keys())[0]
            if id[3] == "2":
                print(f"Add  {id}")
                if not Pants.objects.filter(id=id):

                    # check image in s3
                    addFlag = False
                    for q, img_url in enumerate(j[id]["img"]):
                        img_id = id + "_" + str(q + 1)
                        img = f"pants/{img_id}.jpg"
                        try:
                            s3.get_object(Bucket="dressroom-base-data", Key=img)
                            print(f"Add  {id}", end=" ")
                            addFlag = True
                            break
                        except:
                            pass

                    # if image in s3 create instance
                    if addFlag:
                        pants = Pants.objects.create(
                            id=id,
                            brand=j[id]["brand"],
                            product=j[id]["product"],
                            item_url=j[id]["url"],
                            category=j[id]["sub_category"],
                            shop=j[id]["shop"],
                        )
                    else:
                        continue

                    if len(j[id]["img"]) == 1:
                        img_id = id
                        img = f"pants/{img_id}.jpg"

                        try:
                            s3.get_object(Bucket="dressroom-base-data", Key=img)
                            client_socket.sendall(img.encode())
                            data = client_socket.recv(1024)

                            PantsImage.objects.create(
                                id=img_id,
                                img_url=j[id]["img"][0],
                                img=img,
                                vector=data,
                                pants=pants,
                            )
                            print(f"O", end=" ")
                        except:
                            print(f"X", end=" ")
                            continue

                    else:
                        count = 1
                        for img_url in j[id]["img"][0:1]:
                            img_id = id + "_" + str(count + 1)
                            img = f"pants/{img_id}.jpg"

                            try:
                                s3.get_object(Bucket="dressroom-base-data", Key=img)
                                client_socket.sendall(img.encode())
                                data = client_socket.recv(1024)

                                PantsImage.objects.create(
                                    id=img_id,
                                    img_url=img_url,
                                    img=img,
                                    vector=data,
                                    pants=pants,
                                )
                                count += 1
                                print(f"O", end=" ")
                            except:
                                print(f"X", end=" ")
                                pass
                    print()

        self.stdout.write(
            self.style.SUCCESS(f"All items from file({file}) is added to Database!")
        )

