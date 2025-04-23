import cv2
import time
from rknnpool import rknnPoolExecutor
# 图像处理函数，实际应用过程中需要自行修改
from func import myFunc

cap = cv2.VideoCapture('./720p90.mp4')
# cap = cv2.VideoCapture('/dev/video-camera0')
# 设置分辨率，例如设置为640x480
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
# 设置帧率，例如设置为30FPS
# cap.set(cv2.CAP_PROP_FPS, 60)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"分辨率：{width}x{height}")
print(f"帧率：{fps}")

modelPath = "./rknnModel/yolov5s_relu.rknn"
# modelPath = "./rknnModel/yolov5n.rknn"
# modelPath = "./rknnModel/yolov5s.rknn"
# modelPath = "./rknnModel/yolov5m.rknn"

# 线程数, 增大可提高帧率
TPEs = 6 
# 初始化rknn池
pool = rknnPoolExecutor(
    rknnModel=modelPath,
    TPEs=TPEs,
    func=myFunc)

# 初始化异步所需要的帧
if (cap.isOpened()):
    for i in range(TPEs + 1):
        ret, frame = cap.read()
        if not ret:
            cap.release()
            del pool
            exit(-1)
        pool.put(frame)

frames, loopTime, initTime = 0, time.time(), time.time()
while (cap.isOpened()):
    frames += 1
    ret, frame = cap.read()
    if not ret:
        break
    pool.put(frame)
    frame, flag = pool.get()
    if flag == False:
        break
    cv2.imshow('test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if frames % 30 == 0:
        print("30帧平均帧率:\t", 30 / (time.time() - loopTime), "帧")
        loopTime = time.time()

print("总平均帧率\t", frames / (time.time() - initTime))
# 释放cap和rknn线程池
cap.release()
cv2.destroyAllWindows()
pool.release()
