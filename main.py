import cv2
import cvzone

# Code for opening the webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    imgBG = cv2.imread("Resources/bg.jpg")


    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.imshow("bg", imgBG)
    cv2.waitKey(1)