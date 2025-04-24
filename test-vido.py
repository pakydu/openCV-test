import cv2

# 读取图片
image = cv2.imread("cc4e23eb96b5bc350c0ce182a56ddc52.jpg")  # 替换为你的图片路径

# 打开视频文件
# video_path = "1.mp4"  # 替换为你的视频路径
# cap = cv2.VideoCapture(video_path)

# # 检查视频是否成功打开
# if not cap.isOpened():
#     print("无法打开视频文件！")
#     exit()

# # 获取视频属性
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # 创建视频写入对象（保存处理后的视频）
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter("output.avi", fourcc, fps, (width, height))

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break  # 视频结束

#     # 对每一帧进行处理（例如转为灰度）
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # 转回BGR格式以便显示彩色（灰度图显示为黑白）
#     gray_frame_bgr = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

#     # 写入处理后的帧
#     out.write(gray_frame_bgr)

#     # 显示实时处理结果
#     cv2.imshow("Processed Video", gray_frame_bgr)
#     if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):  # 按 'q' 键退出
#         break

# # 释放资源
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# 打开摄像头（0表示默认摄像头）
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头！")
    exit()

# 设置摄像头分辨率（可选）
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 高度

# 初始化视频写入对象
# fourcc = cv2.VideoWriter_fourcc(*'XVID') #编码方式vid，也可以使用mp4:mp4v
fourcc = cv2.VideoWriter_fourcc(*'mp4v') #编码方式vid，也可以使用mp4:mp4v
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

# while True:
#     # 读取一帧
#     ret, frame = cap.read()
    
#     # 检查是否成功读取帧
#     if not ret:
#         print("无法获取帧！")
#         break

#     # 显示实时画面
#     cv2.imshow('Camera Stream', frame)

#     # 按下 'q' 键退出循环
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # cv2.putText("face")
    
    out.write(frame)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
