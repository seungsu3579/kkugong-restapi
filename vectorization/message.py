# -*- coding:utf-8 -*-
import numpy as np
import socket
from utils import timelog


class Message:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))

    def __del__(self):
        self.client_socket.close()

    # @logging_time
    def imgToVector(self, img):
        # img : 이미지 이름(url)

        self.client_socket.sendall(img.encode())
        data = self.client_socket.recv(1024)
        vector = np.frombuffer(data, dtype=np.float32).reshape(1, 64)

        return vector

    def imgToBit(self, img):
        # img : 이미지 이름(url)

        self.client_socket.sendall(img.encode())
        data = self.client_socket.recv(1024)

        return data

    def bitToVector(self, data):

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

    def recommend_cody(self, data):
        self.client_socket.sendall(data)
        data = self.client_socket.recv(32768)
        data = np.frombuffer(data, dtype=np.int64).reshape(-1, 4)
        data = data.tolist()
        return data

    def recommend_item(self, data):
        self.client_socket.sendall(data)
        data = self.client_socket.recv(32768)
        data = data.decode()

        items = data.split("$")

        for i in range(len(items)):
            items[i] = items[i].split("#")
            items[i][1] = items[i][1].split("/")

        print(items)

        return items
