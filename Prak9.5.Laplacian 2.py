import cv2

# load citra
img = cv2.imread('tugas.jpeg', 0)

# aplikasikan gaussian
blur = cv2.GaussianBlur(img, (3, 3), 0)

# aplikasikan laplacian
laplacian = cv2.Laplacian(blur, cv2.CV_64F)
laplacian = laplacian/laplacian.max()

cv2.imshow('laplacian-gaussian', laplacian)
cv2.waitKey(0)
