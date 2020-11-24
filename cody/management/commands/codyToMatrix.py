import json
from django.core.management.base import BaseCommand
from cody.models import Cody
from config import settings
import socket
import boto3
import numpy as np
import pandas as pd


class Command(BaseCommand):

    help = "Add cody to Database"

    def handle(self, *args, **options):

        columns = []
        columns.append("id")
        for k in range(64):
            col = f"top_col{k}"
            columns.append(col)
        for k in range(64):
            col = f"pants_col{k}"
            columns.append(col)
        for k in range(64):
            col = f"shoes_col{k}"
            columns.append(col)

        matrix = []
        for cody in Cody.objects.all():
            row = list()
            row.append(cody.id)
            print(cody.id)

            img_top = cody.cody_top_img.name
            if img_top != "":
                client_socket_top = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket_top.connect(
                    (settings.TOP_VECTORIZATION_HOST, settings.TOP_VECTORIZATION_PORT)
                )
                client_socket_top.sendall(img_top.encode())
                data_top = client_socket_top.recv(1024)
                client_socket_top.close()
                vector_top = np.frombuffer(data_top, dtype=np.float32).reshape(1, 64)

                for i in range(64):
                    row.append(vector_top[0][i])
            else:
                for i in range(64):
                    row.append(None)

            img_pants = cody.cody_pants_img.name
            if img_pants != "":
                client_socket_pants = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket_pants.connect(
                    (
                        settings.PANTS_VECTORIZATION_HOST,
                        settings.PANTS_VECTORIZATION_PORT,
                    )
                )
                client_socket_pants.sendall(img_pants.encode())
                data_pants = client_socket_pants.recv(1024)
                client_socket_pants.close()
                vector_pants = np.frombuffer(data_pants, dtype=np.float32).reshape(
                    1, 64
                )

                for i in range(64):
                    row.append(vector_pants[0][i])
            else:
                for i in range(64):
                    row.append(None)

            img_shoes = cody.cody_shoes_img.name
            if img_shoes != "":
                client_socket_shoes = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket_shoes.connect(
                    (
                        settings.SHOES_VECTORIZATION_HOST,
                        settings.SHOES_VECTORIZATION_PORT,
                    )
                )
                client_socket_shoes.sendall(img_shoes.encode())
                data_shoes = client_socket_shoes.recv(1024)
                client_socket_shoes.close()
                vector_shoes = np.frombuffer(data_shoes, dtype=np.float32).reshape(
                    1, 64
                )

                for i in range(64):
                    row.append(vector_shoes[0][i])
            else:
                for i in range(64):
                    row.append(None)

            matrix.append(row)

        df = pd.DataFrame(matrix, columns=columns)
        df.to_csv("./matrix_cody.csv", encoding="utf-8")

        self.stdout.write(self.style.SUCCESS(f"All cody is changed to csv!"))

