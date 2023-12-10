print("hi there i m ankita")
print("hi there i am using ")
import cv2 
img = cv2.imread(r"C:\Users\ankita\Downloads\R.png")
print(img)
cv2.imshow("tmp",img)
cap = cv2.VideoCapture(0)

while True:
    _,frame =cap.read()
    print("hiiii")
    cv2.imshow("frame",frame )
    key=cv2.waitKey(1)
    if key ==27:
        break
    
cap.release()
cv2.destroyAllWindows()
