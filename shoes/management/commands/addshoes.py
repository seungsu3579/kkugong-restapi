import json
from django.core.management.base import BaseCommand
from shoes.models import Shoes, ShoesImage
from config import settings
import socket


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
            (settings.SHOES_VECTORIZATION_HOST, settings.SHOES_VECTORIZATION_PORT)
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
            if id[3] == "3":
                print(f"Add  {id}")
                if not Shoes.objects.filter(id=id):
                    shoes = Shoes.objects.create(
                        id=id,
                        brand=j[id]["brand"],
                        product=j[id]["product"],
                        item_url=j[id]["url"],
                    )
                    if len(j[id]["img"]) == 1:
                        img_id = id
                        img = f"shoes/{img_id}.jpg"

                        try:
                            s3.get_object(Bucket="dressroom-base-data", Key=img)

                            client_socket.sendall(img.encode())
                            data = client_socket.recv(1024)

                            ShoesImage.objects.create(
                                id=img_id,
                                img_url=j[id]["img"][0],
                                img=img,
                                vector=data,
                                shoes=shoes,
                            )
                        except:
                            continue

                    else:
                        count = 1
                        for img_url in j[id]["img"]:
                            img_id = id + "_" + str(count + 1)
                            img = f"shoes/{img_id}.jpg"

                            try:
                                s3.get_object(Bucket="dressroom-base-data", Key=img)

                                client_socket.sendall(img.encode())
                                data = client_socket.recv(1024)

                                ShoesImage.objects.create(
                                    id=img_id,
                                    img_url=img_url,
                                    img=img,
                                    vector=data,
                                    shoes=shoes,
                                )
                                count += 1
                            except:
                                pass

        self.stdout.write(
            self.style.SUCCESS(f"All items from file({file}) is added to Database!")
        )

