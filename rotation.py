import cv2

image = cv2.imread('me.jpg')

height, width = image.shape[:2]

# Merubah sudut rotasi menjadi 90 derajat
angle = 90

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imwrite('original_image.jpg', image)
cv2.imwrite('rotated_image.jpg', rotated_image)