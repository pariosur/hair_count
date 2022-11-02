import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

def counter(image_name):

    path = '/uploads/' + image_name
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(15,15),0)
    canny = cv2.Canny(blur, 20, 20,3)
    dilated = cv2.dilate(canny, (1,1), iterations=2)
    (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1,(0,255,0),2)
    plt.imshow(rgb)
    count = len(cnt)

    return f'Hairs in image: {count}'
