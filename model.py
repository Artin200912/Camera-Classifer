from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL
from PIL import Image

class Model:

    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = np.array([])
        class_list = np.array([])

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg')[:, :, 0]

            img = cv.resize(img, (120, 120))
            img = img.reshape(14400) 
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 1)

        for i in range(1, counters[1]):
            img = cv.imread(f'2/frame{i}.jpg')[:, :, 0]
            img = cv.resize(img, (120, 120))
            img = img.reshape(14400) 
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 2)

        img_list = img_list.reshape(counters[0] - 1 + counters[1] - 1, 14400)
        self.model.fit(img_list, class_list)
        print("Model successfully trained!")


    def predict(self, frame):
        frame = frame[1]
        cv.imwrite("frame.jpg", cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        img = Image.open("frame.jpg")
        img = img.resize((120, 120), Image.Resampling.LANCZOS) 
        img.save("frame.jpg")

        img = cv.imread('frame.jpg')[:, :, 0]
        img = img.reshape(14400)
        prediction = self.model.predict([img])

        return prediction[0]
