import json
from django.core.management.base import BaseCommand
from pants.models import Pants, PantsImage
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
        TOP_HOST = "172.17.0.2"
        TOP_PORT = 10001
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((TOP_HOST, TOP_PORT))
        ################

        with open(file, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        for j in json_data:
            id = list(j.keys())[0]
            if id[3] == "2":
                print(f"Add  {id}")
                if not Pants.objects.filter(id=id):
                    pants = Pants.objects.create(
                        id=id,
                        brand=j[id]["brand"],
                        product=j[id]["product"],
                        item_url=j[id]["url"],
                    )
                    if len(j[id]["img"]) == 1:
                        img_id = id
                        img_dir = MEDIA_DIR + "/pants/" + img_id + ".jpg"
                        img = f"pants/{img_id}.jpg"

                        client_socket.sendall(img_dir.encode())
                        data = client_socket.recv(1024)

                        PantsImage.objects.create(
                            id=img_id,
                            img_url=j[id]["img"][0],
                            img=img,
                            vector=data,
                            pants=pants,
                        )
                    else:
                        for i, img in enumerate(j[id]["img"]):
                            img_id = id + "_" + str(i + 1)
                            img_dir = MEDIA_DIR + "/pants/" + img_id + ".jpg"
                            img = f"pants/{img_id}.jpg"

                            client_socket.sendall(img_dir.encode())
                            data = client_socket.recv(1024)

                            PantsImage.objects.create(
                                id=img_id,
                                img_url=img,
                                img=img,
                                vector=data,
                                pants=pants,
                            )
        self.stdout.write(
            self.style.SUCCESS(f"All items from file({file}) is added to Database!")
        )

