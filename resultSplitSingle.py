import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
DateFrame = pd.read_table('/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/comp4_det_test_baseball-diamond.txt',delimiter=' ', header=None, sep=' ', names=["image_name", "score", "left", "top", "right", "bottom"])



class evluation():

    def __init__(self):
        '''

        DateFrame = pd.read_table(path='/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/comp4_det_test_baseball-diamond.txt',
                   delimiter=' ', header=None, sep=' ', names=["image_name", "score", "left", "top", "right", "bottom"])
        '''

        df = DateFrame.drop(labels='score', axis=1)
        df = df.to_csv('/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/baseball-diamond.txt', sep=' ', header=None, index=False)
        all = pd.read_table('/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/baseball-diamond.txt',
                   delimiter=' ', header=None, sep=' ', names=["image_name", "left", "top", "right", "bottom"])
        image_name = all['image_name']

        dd = all.drop(labels='image_name', axis=1)
        dd = dd.to_csv('/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/baseball-diamond/results.txt', sep=' ', header=None, index=False)


        img = []
        for i in range(0, len(image_name)):
            img.append(image_name.iloc[i])
        such = []
        for i in img:
            index = [x for x in range(len(img)) if img[x] == i]
            such.append([i, index])
        final = list(such)

        m = pd.read_table('/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/baseball-diamond/results.txt', header=None, sep=' ', names=["left", "top", "right", "bottom"])
        m.insert(0,'class_name', 'baseball-diamond')
        #print(m)

        '''
        Now, it's going to make single txt with foto name
        '''
        for i in range(len(final)):
            imn = final[i][0]
            index = final[i][1]
            for j in range(len(index)):
                p = index[0]
                q = index[j]
                n = m.loc[p:q]
                jieguo = n.to_csv(
                    '/home/dingjin/ObjectDetection-OneStageDet/yolo/results/Yolov3/baseball-diamond/' + imn + '.txt',
                    header=None, sep=' ', index=None)

Step = evluation()



