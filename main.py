import cv2
import os
import pickle
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')
folderModePath ='Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = [] 
#importing the mode images into the list
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
#print(len(imgModeList))
#Load the encoding file
file = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, StudentIds = encodeListKnownWithIds
print(StudentIds)
while True:
    success, img = cap.read()

    imgBackground[162:162+480,55:55+640] = img #Length and height of the camera images
    imgBackground[44:44+633,808:808+414] = imgModeList[2]
    #cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance",imgBackground)
    cv2.waitKey(1)
