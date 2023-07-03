import cv2
import face_recognition
import pickle
import os
#Importing student images
imgBackground = cv2.imread('Resources/background.png')
folderPath ='Images'
PathList = os.listdir(folderPath)
imgList = []
# print(PathList) 
#importing the mode images into the list
studentIds = []

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
   # print(path)
   # print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])
#print(len(imgList))

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    
    return encodeList

print("Encoding started....")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown,studentIds]
print(encodeListKnown)
print("Encoding complete")

file = open("EncodeFile.p","wb")
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File saved")








































