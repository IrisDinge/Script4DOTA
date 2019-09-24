import pandas as pd

data = pd.read_csv("/home/dingjin/Yolov3_DOTA/yolo/results/comp4_det_test_baseball-diamond.txt",
                   sep=' ', names=['image', 'score', 'x', 'y', 'w', 'h'])

#df = data.drop(columns='score')
data.insert(loc=1, column='id', value='baseball-diamond')
data.to_csv("/home/dingjin/Yolov3_DOTA/yolo/results/merge/baseball-diamond.txt", sep=' ', header=None, index=None)
print(data)
