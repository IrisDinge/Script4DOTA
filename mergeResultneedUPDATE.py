import pandas as pd
import os


labels = ["small-vehicle",
          "large-vehicle",
          "plane",
          "harbor",
          "ship",
          "helicopter",
          "bridge",
          "swimming-pool",
          "baseball-diamond",
          "roundabout",
          "tennis-court",
          "storage-tank",
          "soccer-ball-field",
          "basketball-court",
          "ground-track-field",
          "container-crane"]


for i in labels:
    data = pd.read_table("/home/dingjin/Yolov3_DOTA/yolo/results/Yolov3_JPEG800/" + "comp4_det_test_" + i + ".txt",
                         sep=' ', names=['image', 'score', 'x', 'y', 'w', 'h'])
    data.insert(loc=1, column='id', value=i)
    data.to_csv("/home/dingjin/Yolov3_DOTA/yolo/results/Yolov3_JPEG800/merge/" + i + ".txt", sep=' ',
                header=None, index=None)
    #print(i)

'''

labels = ["small-vehicle",
          "large-vehicle",
          "plane",
          "harbor",
          "ship",
          "helicopter",
          "bridge",
          "swimming-pool",
          "baseball-diamond",
          #"roundabout",
          #"tennis-court",
          #"storage-tank",
          #"soccer-ball-field",
          #"basketball-court",
          #"ground-track-field",
          #"container-crane"]

data = pd.read_csv("/home/dingjin/Yolov3_DOTA/yolo/results/comp4_det_test_baseball-diamond.txt",
                   sep=' ', names=['image', 'score', 'x', 'y', 'w', 'h'])

#df = data.drop(columns='score')
data.insert(loc=1, column='id', value='baseball-diamond')
data.to_csv("/home/dingjin/Yolov3_DOTA/yolo/results/merge/baseball-diamond.txt", sep=' ', header=None, index=None)
print(data)
'''
