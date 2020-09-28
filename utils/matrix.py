import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from tops.models import TopsImage
from pants.models import PantsImage
from shoes.models import ShoesImage
import numpy as np
import pandas as pd
from vectorization.message import Message


class Matrix:
    def bitToVector(self, data):
        vector = np.frombuffer(data, dtype=np.float32).reshape(1, 64)
        return vector

    def topMatrixToCsv(self):
        matrix = []
        for img in TopsImage.objects.all():
            row = list()
            row.append(img.id)

            if img.vector == b"":
                continue

            vector = self.bitToVector(img.vector)
            for i in range(64):
                row.append(vector[0][i])

            matrix.append(row)

        columns = []
        columns.append("id")
        for k in range(64):
            col = f"col{k}"
            columns.append(col)

        df = pd.DataFrame(matrix, columns=columns)
        df.to_csv("./matrix_top.csv", encoding="utf-8")

        print("top image vector >> csv matrix")

    def pantsMatrixToCsv(self):
        matrix = []
        for img in PantsImage.objects.all():
            row = list()
            row.append(img.id)

            if img.vector == b"":
                continue

            vector = self.bitToVector(img.vector)
            for i in range(64):
                row.append(vector[0][i])

            matrix.append(row)

        columns = []
        columns.append("id")
        for k in range(64):
            col = f"col{k}"
            columns.append(col)

        df = pd.DataFrame(matrix, columns=columns)
        df.to_csv("./matrix_pants.csv", encoding="utf-8")

        print("pants image vector >> csv matrix")

    def shoesMatrixToCsv(self):
        matrix = []
        for img in ShoesImage.objects.all():
            row = list()
            row.append(img.id)

            if img.vector == b"":
                continue

            vector = self.bitToVector(img.vector)
            for i in range(64):
                row.append(vector[0][i])

            matrix.append(row)

        columns = []
        columns.append("id")
        for k in range(64):
            col = f"col{k}"
            columns.append(col)

        df = pd.DataFrame(matrix, columns=columns)
        df.to_csv("./matrix_shoes.csv", encoding="utf-8")

        print("shoes image vector >> csv matrix")

    def topMatrixToNPY(self):
        matrix = "0"
        for img in TopsImage.objects.all():
            if matrix == "0":
                data = img.vector
                if data == b"":
                    continue
                else:
                    matrix = self.bitToVector(data)
            else:
                data = img.vector
                print(data)
                if data == b"":
                    continue
                else:
                    vector = self.bitToVector(data)
                    matrix = np.append(matrix, vector, axis=0)

        np.save("./matrix_top.npy", matrix)

        print("top image vector >> npy matrix")
        print("Complete")

    def npyToMatrix(self, dir):
        matrix = np.load(dir)
        return matrix

