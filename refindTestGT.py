import os
import shutil





for line in open("/home/dingjin/Yolov3_DOTA/yolo/dota/DOTA/ImageSets/Main/test.txt"):
    img_name = line.strip('\n')
    file_name = "/home/dingjin/Yolov3_DOTA/yolo/dota/groundtruth/labels/" + img_name + ".txt"
    test_file = "/home/dingjin/Yolov3_DOTA/yolo/dota/groundtruth/testGT/" + img_name + ".txt"
    print(test_file)
    shutil.copyfile(file_name, test_file)

