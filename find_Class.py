#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import glob
import sys
from xml.dom.minidom import parse
import xml.dom.minidom as xmldom

def parse_xml(path):

    if(os.path.exists(path)):

        fn = glob.glob(path + "*")
        print(fn)


        for file in fn:
            print(file)

            xml_file = xmldom.parse(file)
            eles = xml_file.documentElement
    #print(eles.tagName)
            n = len(eles.getElementsByTagName("name"))
    #print(n)
            for i in range(n):
                image_name = eles.getElementsByTagName("filename")[0].firstChild.data
                class_name = eles.getElementsByTagName("name")[i].firstChild.data
            if class_name == "container-crane":
                print(image_name, class_name)
                break
            else:
                print("it's ok")

if __name__=="__main__":
    parse_xml('/home/dingjin/Yolov3_DOTA/yolo/dota/DOTA/Annotations/')
