import cv2
import numpy as np
from matplotlib import pyplot as plt

def compute_harris_response(im, sigma=3):
    im = rgb2gray(im)
    imx = np.zeros(im.shape)
    imy = np.zeros(im.shape)
    filters.gaussian_filter(im, (sigma, sigma), (0, 1), imx)
    filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)

    Wxx = filters.gaussian_filter(imx*imx, sigma)
    Wxy = filters.gaussian_filter(imx*imy, sigma)
    Wyy = filters.gaussian_filter(imy*imy, sigma)

    Wdet = Wxx*Wyy - Wxy**2
    Wtr = Wxx + Wyy

    return Wdet/Wtr

def get_harris_points(harrisim, min_dist=10, threshold=0.1):
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1
    coords = np.array(harrisim_t.nonzero()).T

    candidate_values = [harrisim[c[0], c[1]] for c in coords]
    index = np.argsort(candidate_values)

    allowed_locations = np.zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1

    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i,0], coords[i,1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),
                              (coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0
    
    return filtered_coords

def get_descriptors(image, filtered_coords, wid=5):
    desc = []
    for coords in filtered_coords:
        patch = image[
                      coords[0] - wid : coords[0] + wid + 1,
                      coords[1] - wid : coords[1] + wid + 1
        ].flatten()
        desc.append(patch)
    
    return desc

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
