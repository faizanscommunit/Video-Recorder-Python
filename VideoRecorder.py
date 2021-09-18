#**** ---- Note --- ****#
# Video Recorder - Python
# By Faizanscommunit
# MIT Licensed

#**** --- Source Code --- ****#
import cv2
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter(
    'recorded_video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width, height))
while True:
    _, frame = cap.read()
    writer.write(frame)
    cv2.imshow('Video Recorder', frame)
    if cv2.waitKey(10) == ord('q'):
        break
        
#**** --- Social Links --- ****#
#  Github: https://github.com/faizanscommunit
#  Fiverr: https://fvrr.co/3iZIX0L
#  Website: https://faizanscommunit.pythonanywhere.com/
#  Instagram: https://www.instagram.com/faizanscommunit/
