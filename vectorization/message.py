# -*- coding:utf-8 -*-
import socket
from utils import timelog


class Message:
    def __init__(self, host, port):
        self.TOP_HOST = host
        self.TOP_PORT = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.TOP_HOST, self.TOP_PORT))

    def __del__(self):
        self.client_socket.close()

    # @logging_time
    def imgToVector(self, img):
        # img : 이미지 이름(url)
        import numpy as np

        self.client_socket.sendall(img.encode())
        data = self.client_socket.recv(1024)
        vector = np.frombuffer(data, dtype=np.float32).reshape(1, 64)

        return vector

    def imgToBit(self, img):
        # img : 이미지 이름(url)
        import numpy as np

        self.client_socket.sendall(img.encode())
        data = self.client_socket.recv(1024)

        return data

    def bitToVector(self, data):
        import numpy as np

        vector = np.frombuffer(data, dtype=np.float32).reshape(1, 64)
        return vector

    def recommand(self, data):
        self.client_socket.sendall(data)
        data = self.client_socket.recv(1024)
        recommands = data.decode().split(",")
        img_ids = []
        for img_id in recommands:
            if len(img_id) == 13:
                img_id = img_id[:-1] + "_" + img_id[-1]
            img_ids.append(img_id)

        return img_ids

