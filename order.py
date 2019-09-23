import pandas as pd
import numpy as np


data = pd.read_table("/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/empty.txt",
                     sep=' ', names=["image_name", "id", "left", "top", "right", "bottom"])
new = data.groupby(data['image_name'])
#print(new.size())

for name, group in new:
    #print(name)
    #print(type(group))
    group.to_csv("/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/test/" + name + ".txt",
                 sep=' ', header=None, index=None)
