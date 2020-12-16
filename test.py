import cv2

src = cv2.imread("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_006.JPG", cv2.IMREAD_COLOR)

height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 15, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_15.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 30, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_30.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_45.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 60, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_60.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 75, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_75.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_90.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 105, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_105.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 120, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_120.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 135, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_135.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 150, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_150.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 165, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_165.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_180.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 195, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_195.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 210, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_210.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 225, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_225.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 240, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_240.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 255, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_255.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 270, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_270.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 285, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_285.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 300, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_300.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 315, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_315.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 330, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_330.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

matrix = cv2.getRotationMatrix2D((width/2, height/2), 345, 1)
dst = cv2.warpAffine(src, matrix, (width, height))
cv2.imwrite("C:\\Users\\82104\\Desktop\\OBJ_lighters\\lighter_005_345.JPG", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()







