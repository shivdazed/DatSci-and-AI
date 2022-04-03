#check email dates if any
import cv2

face_cascade=cv2.CascadeClassifier("/Users/purnimagebhardt/Downloads/opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml")

a = cv2.VideoCapture(0)

#a = cv2.VideoCapture(r"/Users/purnimagebhardt/Downloads/Faces from around the world.mp4")


while(1):
    st,pix=a.read()
    if st == False:
        break
    gray_imag= cv2.cvtColor(pix,cv2.COLOR_BGR2GRAY)
    face_=face_cascade.detectMultiScale(gray_imag, 2, 3)
    print(face_)
    for(x, y, w, h) in face_:
        cv2.rectangle(pix, (x, y), (x+w,y+h),(0,255,0),5)
        cv2.putText(gray_imag,'FaceFound',(0,20),cv2.FONT_ITALIC,2,color=(0,0,255))

    cv2.imshow('windowqqq',pix);
    b = cv2.waitKey(50)
    if b == ord('q'):
        cv2.destroyAllWindows()
        break

a.release()
