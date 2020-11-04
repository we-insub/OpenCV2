import cv2
imageFile= './data/lena.jpg'
img=cv2.imread(imageFile)
#bgr 포맷으로 읽어서 img객체에 저장한다
cv2.imwrite('./data/Lena.bmp',img)
cv2.imwrite('./data/Lena2.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])
#Lena2.png 이름으로 파일저장 0~9 사이의 숫자로 압축률 저장한다 기폴트(기본값)3
cv2.imwrite('./data/Lena2.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,90])
#Lena2.jpg 이름으로 파일저장한다 . jpg의 품질을 90%으로 설정한다 디폴트는 95%
