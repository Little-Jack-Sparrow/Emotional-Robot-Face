# 极简人脸检测Demo（我的第一个入门项目）
# 运行前请先安装：pip install opencv-python
import cv2

# 加载OpenCV自带的人脸检测预训练模型
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 打开电脑摄像头（0是默认摄像头）
cap = cv2.VideoCapture(0)

print("人脸检测已启动，按q键退出")

while True:
    # 读取摄像头画面
    ret, frame = cap.read()
    if not ret:
        break
    
    # 转为灰度图，提升检测效率
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # 在画面上框出人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Face Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    # 显示画面
    cv2.imshow('Face Detection Demo', frame)
    
    # 按q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()