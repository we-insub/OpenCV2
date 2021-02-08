import cv2

vidcap = cv2.VideoCapture("C:\\Users\\82104\\Desktop\\video\\IMG_4532.mp4")
count = 0

while (vidcap.isOpened()):
    ret, image = vidcap.read()
    # 이미지 사이즈 960x540으로 변경
    # image = cv2.resize(image, (960, 540))

    # 30프레임당 하나씩 이미지 추출
    if (int(vidcap.get(1)) % 5 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        # 추출된 이미지가 저장되는 경로
        cv2.imwrite("C:\\Users\\82104\\Desktop\\video\\test\\fream%d.JPG" % count, image)
        # print('Saved frame%d.jpg' % count)
        count += 1

vidcap.release()