import json
from django.core.management.base import BaseCommand
from shoes.models import Shoes, ShoesImage
from config import settings

import socket
import numpy as np


class Command(BaseCommand):

    help = "Add json data to Database"

    def add_arguments(self, parser):
        parser.add_argument("--filename", help="json file to add")

    def handle(self, *args, **options):
        file = options.get("filename")
        MEDIA_DIR = settings.MEDIA_ROOT

        #### socket ####
        TOP_HOST = "172.17.0.2"
        TOP_PORT = 9999
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((TOP_HOST, TOP_PORT))
        ################

        with open(file, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        for j in json_data:
            _id = list(j.keys())[0]
            if _id[3] == "3":
                print(f"Add  {_id}")
                if not Shoes.objects.filter(_id=_id):
                    shoes = Shoes.objects.create(
                        _id=_id,
                        brand=j[_id]["brand"],
                        product=j[_id]["product"],
                        item_url=j[_id]["url"],
                    )
                    if len(j[_id]["img"]) == 1:
                        img_id = _id
                        img_dir = MEDIA_DIR + "/shoes/" + img_id + ".jpg"

                        client_socket.sendall(img_dir.encode())
                        data = client_socket.recv(1024)

                        ShoesImage.objects.create(
                            _id=img_id,
                            img_url=j[_id]["img"][0],
                            img_dir=img_dir,
                            vector=data,
                            shoes=shoes,
                        )
                    else:
                        for i, img in enumerate(j[_id]["img"]):
                            img_id = _id + "_" + str(i + 1)
                            img_dir = MEDIA_DIR + "/shoes/" + img_id + ".jpg"

                            client_socket.sendall(img_dir.encode())
                            data = client_socket.recv(1024)

                            ShoesImage.objects.create(
                                _id=img_id,
                                img_url=img,
                                img_dir=img_dir,
                                vector=data,
                                shoes=shoes,
                            )
        self.stdout.write(
            self.style.SUCCESS(f"All items from file({file}) is added to Database!")
        )

