print("hi there i m ankita")
print("hi there i am using ")
import cv2 
img = cv2.imread(r"C:\Users\ankita\Downloads\R.png")
print(img)
cv2.imshow("tmp",img)
print("showing image")
cap = cv2.VideoCapture(0)

while True:
    _,frame =cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLO_BGR2HSV)
    height,width,_=frame.shape
    cx=int(width/2)
    cy=int(height/2)
    #pick pixel value 
    pixel_center =frame[cy,cx]
    print(pixel center)
    cv2.circle("frame",(cx,cy),5,(255,0,0),3)
    cv2.imshow("frame",frame )
    key=cv2.waitKey(1)
    if key ==27:
        break
    
cap.release()
cv2.destroyAllWindows()
