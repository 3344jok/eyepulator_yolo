import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

print("开始采集照片")
 
cap = cv2.VideoCapture(0)


i=81

while cap.isOpened():
    ret, img = cap.read()
    if ret is not True:
        print("读取失败，退出")
        break      
    #处理img
    cv2.imshow('vedio', img)
    
    #检查按键
    key = cv2.waitKey(20) 
    if  key == ord('q') or key == ord('Q') :
        break
    elif key == ord('c') or key == ord('C'):
        cv2.imwrite("./clr/"+str(i)+".jpg",img)
        i+=1
        
print('cap.isOpened():',cap.isOpened())
cap.release()
print('cap.isOpened():',cap.isOpened())