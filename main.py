import cv2
import numpy as np
#Reading image
img=cv2.imread("face.jpg")
#Edge Detection
canny=cv2.Canny(img,20,170)
cv2.imshow("Canny",canny)
#Image Pyramid
smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)
cv2.imshow("larger",larger)
cv2.imshow("smaller",smaller)
#Blurred image
kernel=np.ones((7,7),np.float32)/49
blurred=cv2.filter2D(img,-1,kernel)
cv2.imshow("Blurred",blurred)
#Crop Image
height,width=img.shape[:2]
start_row,start_col=int(height*.15),int(width*.15)
end_row,end_col=int(height*.65),int(width*.65)
cropped=img[start_row:end_row,start_col:end_col]
cv2.imshow("Cropped",cropped)
#Capture video
#video=cv2.VideoCapture(0)
#while True:
#    check,frame=video.read()
#    cv2.imshow("frame",frame)
#    cv2.waitKey(0)
#Image Transpose using opencv
transimg=cv2.transpose(img)
cv2.imshow("Transpose Image",transimg)
#Rotate image
height, width=img.shape[:2]
rotateimg=cv2.getRotationMatrix2D((width/2,height/2),70,.5)
finalimg=cv2.warpAffine(img,rotateimg,(width,height))
cv2.imshow("Rotated Image",finalimg)
#Image information
print(img.shape)
print("Height:",img.shape[0])
print("Weight:",img.shape[1])
cv2.imshow("Output Image",img)
#Writing image
cv2.imwrite("output.jpg",img)
cv2.waitKey(0)
