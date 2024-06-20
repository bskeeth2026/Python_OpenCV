# Python_OpenCV
This Python code using OpenCV demonstrates various image processing techniques on an image named "face.jpg":

1. Image Reading and Display:
- It reads the image "face.jpg" using `cv2.imread`.
- The original image is displayed using `cv2.imshow("Output Image", img)`.

2. Edge Detection:
- It applies the Canny edge detection algorithm using `cv2.Canny(img, 20, 170)`. The parameters 20 and 170 control the thresholds for edge detection sensitivity.
- The resulting edge image is displayed as "Canny".

3. Image Pyramid:
- It creates a smaller image using image downscaling (`cv2.pyrDown(img)`) and a larger image using upscaling (`cv2.pyrUp(img)`).
- The smaller and larger images are displayed as "smaller" and "larger", respectively.

4. Image Blurring:
- It creates a blurring kernel using `np.ones((7,7),np.float32)/49`. This defines a 7x7 averaging kernel for blurring.
- The blurred image is obtained using `cv2.filter2D(img, -1, kernel)` and displayed as "Blurred".

5. Image Cropping:
- It calculates the start and end rows/columns for cropping, taking 15% of the image height and width from the edges.
- The cropped image is displayed as "Cropped".

6. Video Capture (Commented Out):
- The code includes commented-out lines for capturing video from your webcam using `cv2.VideoCapture(0)`. It reads frames in a loop and displays them.

7. Image Transpose:
- It creates a transposed image using `cv2.transpose(img)`, essentially swapping rows and columns.
- The transposed image is displayed as "Transpose Image".

8. Image Rotation:
- It calculates a rotation matrix for a 70-degree counter-clockwise rotation centered at the image center using `cv2.getRotationMatrix2D`.
- The rotated image is obtained using `cv2.warpAffine` and displayed as "Rotated Image".

9. Image Information:
- The code prints the image shape (`img.shape`), which provides height, width, and number of channels. It also prints the height and width separately.

10. Writing the Original Image:
- Finally, it writes the original image to a new file named "output.jpg" using `cv2.imwrite`.

11. Holding the Display:
- `cv2.waitKey(0)` waits for any key press before closing the windows, allowing you to see the results.

This code provides a good starting point for exploring various OpenCV functionalities for image manipulation. You can modify it to experiment with different image processing techniques, adjust parameters, and explore other OpenCV functions like color space conversions, object detection, and more.
