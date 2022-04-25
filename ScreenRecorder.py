from PIL import ImageGrab
import numpy as numpy
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

while True:
    image = ImageGrab.grab(bbox=(0, 0, width, height))
    image_numpy = numpy.array(image)
    image_final = cv2.cvtColor(image_numpy, cv2.COLOR_BGR2RGB)
    
    web_camera = cv2.VideoCapture(0)
    _, frame = web_camera.read()
    frame_height, frame_width, _ = frame.shape
    image_final[0:frame_height, 0:frame_width, :] = frame [0: frame_height, 0: frame_width, :]

    cv2.imshow('Screen recorder', image_final)
    captured_video.write(image_final)


    
    if cv2.waitKey(10) == ord('q'):
        break