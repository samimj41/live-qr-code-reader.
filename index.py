import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while 1:
    success,img = cap.read()   
    code = decode(img)
    for qrCode in code:
        Text = qrCode.data.decode('utf-8')
        points=np.array([qrCode.polygon],np.int32)
        rp = qrCode.rect
        cv2.polylines(img,[points],True,(0, 255, 0),3)
        cv2.putText(img,Text,(rp[0],rp[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,0,0),1)
        print(Text)
    cv2.imshow('Result' , img)
    cv2.waitKey(2) 