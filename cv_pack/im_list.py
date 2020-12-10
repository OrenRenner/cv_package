import cv2
import numpy as np
from matplotlib import pyplot as plt

#!pip install opencv-python==3.4.2.16
#!pip install opencv-contrib-python==3.4.2.16

def matching_SURF(train_image_path, test_image_path):
    #train_image_path, test_image_path - путь к тренировочному и тестовому изображениям для сопоставления
    assert isinstance(train_image_path, str) and isinstance(test_image_path, str)
    
    train_image = cv2.imread(train_image_path)
    train_image = cv2.cvtColor(train_image, cv2.COLOR_BGR2RGB)
    
    test_image = cv2.imread(test_image_path)
    test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
    
    #Метод SURF для выделения ключевых точек на изображении
    orb2 = cv2.xfeatures2d_SURF.create() 

    kp1, des1 = orb2.detectAndCompute(train_image, None)
    kp2, des2 = orb2.detectAndCompute(test_image, None)
    
    #Метод knn для сопоставления дискрипторов изображения
    bf = cv2.BFMatcher()
    mathes = bf.knnMatch(des1, des2, k=2)
    
    good = []
    for m,n in mathes:
        if m.distance < 0.5*n.distance:
            good.append([m])
    
    img3 = cv2.drawMatchesKnn(train_image, kp1, test_image, kp2, good[:30], None, matchColor=(255, 0, 0), matchesMask=None,
                              singlePointColor=(0, 0, 255), flags=0)
    img4 = cv2.drawMatchesKnn(train_image, kp1, test_image, kp2, good[:30], None, matchColor=(255, 0, 0), matchesMask=None,
                              singlePointColor=(0, 0, 255), flags=2)
    
    return im3, img4
