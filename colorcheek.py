import cv2 #파이썬에서 openCV를 사용하기 위해
from matplotlib import pyplot as plt
#matplotib 패키지에서 pyplot 를 pit 라는 이름으로 임포트한다.

imageFile ='./data/lena.jpg'

imgBGR=cv2.imread(imageFile) #cv.IMREAD_COLOR
#이미지는 R G B 가 있는데 0 으로 들어가면 그레이스케일으로 보기로 한다.


#X,Y 축을 표시하지 않는다.
plt.axis('off')
plt.imshow(imgBGR)
plt.show()

#imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
#plt.imshow(imgRGB) #plot에 imgRGB를 그리고
#plt.show() # plot에 그린 내용을 출력한다.
