import cv2
imageFile ='./data/lena.jpg'

img=cv2.imread(imageFile) #cv.IMREAD_COLOR
img2=cv2.imread(imageFile,0) #cv2.IMREAD_GRAYSCALE
#이미지는 R G B 가 있는데 0 으로 들어가면 그레이스케일으로 보기로 한다.
cv2.imshow('lena Color',img) #lena color이라는 윈도우 생성
cv2.imshow('lena grayscale',img2) # lena 그레이스케일

cv2.waitKey()
cv2.destroyAllWindows()