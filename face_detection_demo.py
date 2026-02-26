# 极简人脸检测Demo（我的第一个入门项目）
# 运行前请先安装：pip install opencv-python
import cv2

# 加载OpenCV自带的人脸检测预训练模型
# 路径兼容不同系统，避免找不到模型文件的问题
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# 打开电脑摄像头（0是默认摄像头）
# 添加CAP_DSHOW参数，解决Windows系统摄像头启动慢/黑屏问题
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 设置摄像头画面尺寸（可选，提升效率）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("人脸检测已启动，按q键退出")

while True:
    # 读取摄像头画面
    ret, frame = cap.read()
    if not ret:
        print("无法读取摄像头画面，程序退出")
        break
    
    # 转为灰度图，提升检测效率（人脸检测对灰度图更敏感）
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 检测人脸（优化参数：减少误检、避免重复框）
    # scaleFactor：每次缩放比例；minNeighbors：邻域数（越大误检越少）；minSize：最小检测人脸尺寸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15,    # 小幅提高缩放比例，减少重复检测
        minNeighbors=6,      # 提高邻域数，过滤误检框
        minSize=(50, 50)     # 增大最小尺寸，忽略小的误检区域
    )
    
    # 在画面上框出人脸
    for (x, y, w, h) in faces:
        # 绿色矩形框（BGR格式：0,255,0），线宽2
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 人脸上方添加文字标注
        cv2.putText(
            frame, 
            "Face Detected", 
            (x, y-10),          # 文字位置（人脸框上方10像素）
            cv2.FONT_HERSHEY_SIMPLEX,  # 字体
            0.9,                 # 字体大小
            (0, 255, 0),         # 文字颜色（绿色）
            2                    # 文字线宽
        )
    
    # 显示画面窗口
    cv2.imshow('Face Detection Demo (按q退出)', frame)
    
    # 按q键退出（兼容大小写，避免卡键）
    if cv2.waitKey(1) & 0xFF in [ord('q'), ord('Q')]:
        break

# 释放摄像头资源，关闭所有窗口（避免占用摄像头）
cap.release()
cv2.destroyAllWindows()
print("人脸检测程序已正常退出")