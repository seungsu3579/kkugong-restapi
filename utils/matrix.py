from vectorization.message import Message
from tops.models import TopsImage
from pants.models import PantsImage
from shoes.models import ShoesImage
import numpy as np


class Matrix:
    def bitToVector(self, data):
        vector = np.frombuffer(data, dtype=np.float32).reshape(1, 50)
        return vector

    # def topMatrixToCsv(self):
    #     print("========= STEP 1 (TOP) =========")
    #     matrix = []
    #     for img in TopsImage.objects.all():
    #         row = list()
    #         row.append(img._id)

    #         vector = bitToVector(img.vector)
    #         for i in range(50):
    #             row.append(vector[0][i])

    #         matrix.append(row)

    #     columns = []
    #     columns.append("id")
    #     for k in range(50):
    #         col = f"col{k}"
    #         columns.append(col)

    #     df = pd.DataFrame(matrix, columns=columns)
    #     df.to_csv("./matrix_top.csv", encoding="utf-8")

    # print("========= STEP 2 (PANTS) =========")

    # print("========= STEP 3 (SHOES) =========")

    def topMatrixToNPY(self):

        print("========= STEP 1 (TOP) =========")
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

    def npyToMatrix(self, dir):
        matrix = np.load(dir)
        return matrix
