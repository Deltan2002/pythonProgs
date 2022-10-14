import cv2 as cv


img = cv.imread(cv.samples.findFile("starry_night.jpg"))
cv.imshow("Display window", img)
k = cv.waitKey(0)
