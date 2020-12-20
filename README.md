# cv_package
Scientific Python


Пакет для сопоставления изображений по ключевым точкам


def matching_SURF(train_image_path, test_image_path) - функция сопоставления

Например:

train_image_path = 'images/place_all.jpg'

<p align="center">
  <img src="index1.png" width="500">
</p>

test_image_path = 'images/place_1.jpg'


<p align="center">
  <img src="index2.png" width="500">
</p>


Далее:

im1, im2 = matching_SURF(train_image_path, test_image_path)

imshow(im1)

<p align="center">
  <img src="index3.png" width="500">
</p>

imshow(im2)

<p align="center">
  <img src="index4.png" width="500">
</p>

Для просмотра ключевых точек используйте функцию
compute_harris_response(im, sigma=3), где im считанное изображение

Например:

<p align="center">
  <img src="index9.png" width="500">
</p>

Результат:

<p align="center">
  <img src="index9.png" width="500">
</p>

