import os
from xml.dom.minidom import Document
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import cv2



'''

DOTA format transform to pascal VOC directly

'''

def WriterXMLFiles(filename, path, box_list, label_list, difficult_list, w, h, d):

    # dict_box[filename]=json_dict[filename]
    doc = xml.dom.minidom.Document()
    root = doc.createElement('annotation')
    doc.appendChild(root)

    foldername = doc.createElement("folder")
    foldername.appendChild(doc.createTextNode("DOTA"))
    root.appendChild(foldername)

    nodeFilename = doc.createElement('filename')
    nodeFilename.appendChild(doc.createTextNode(img_name))
    root.appendChild(nodeFilename)

    sourcename = doc.createElement("source")

    databasename = doc.createElement("database")
    databasename.appendChild(doc.createTextNode("DOTA"))
    sourcename.appendChild(databasename)

    annotationname = doc.createElement("annotation")
    annotationname.appendChild(doc.createTextNode("DOTA"))
    sourcename.appendChild(annotationname)

    imagename = doc.createElement("image")
    imagename.appendChild(doc.createTextNode("DOTA"))
    sourcename.appendChild(imagename)

    flickridname = doc.createElement("flickrid")
    flickridname.appendChild(doc.createTextNode("000000"))
    sourcename.appendChild(flickridname)

    root.appendChild(sourcename)

    nodesize = doc.createElement('size')
    nodewidth = doc.createElement('width')
    nodewidth.appendChild(doc.createTextNode(str(w)))
    nodesize.appendChild(nodewidth)
    nodeheight = doc.createElement('height')
    nodeheight.appendChild(doc.createTextNode(str(h)))
    nodesize.appendChild(nodeheight)
    nodedepth = doc.createElement('depth')
    nodedepth.appendChild(doc.createTextNode(str(d)))
    nodesize.appendChild(nodedepth)
    root.appendChild(nodesize)

    segname = doc.createElement("segmented")
    segname.appendChild(doc.createTextNode("0"))
    root.appendChild(segname)

    for (box, label, difficult) in zip(box_list, label_list, difficult_list):

        nodeobject = doc.createElement('object')
        nodename = doc.createElement('name')
        nodename.appendChild(doc.createTextNode(str(label)))
        nodeobject.appendChild(nodename)

        nodename = doc.createElement('pose')
        nodename.appendChild(doc.createTextNode('Left'))
        nodeobject.appendChild(nodename)

        nodename = doc.createElement('truncated')
        nodename.appendChild(doc.createTextNode('NA'))
        nodeobject.appendChild(nodename)

        nodename = doc.createElement('difficult')
        nodename.appendChild(doc.createTextNode(str(difficult)))
        nodeobject.appendChild(nodename)

        nodebndbox = doc.createElement('bndbox')
        nodex1 = doc.createElement('xmin')
        nodex1.appendChild(doc.createTextNode(str(box[0])))
        nodebndbox.appendChild(nodex1)
        nodey1 = doc.createElement('ymin')
        nodey1.appendChild(doc.createTextNode(str(box[1])))
        nodebndbox.appendChild(nodey1)
        nodex2 = doc.createElement('xmax')
        nodex2.appendChild(doc.createTextNode(str(box[2])))
        nodebndbox.appendChild(nodex2)
        nodey2 = doc.createElement('ymax')
        nodey2.appendChild(doc.createTextNode(str(box[3])))
        nodebndbox.appendChild(nodey2)
        '''
        nodex3 = doc.createElement('x3')
        nodex3.appendChild(doc.createTextNode(str(box[4])))
        nodebndbox.appendChild(nodex3)
        nodey3 = doc.createElement('y3')
        nodey3.appendChild(doc.createTextNode(str(box[5])))
        nodebndbox.appendChild(nodey3)
        nodex4 = doc.createElement('x4')
        nodex4.appendChild(doc.createTextNode(str(box[6])))
        nodebndbox.appendChild(nodex4)
        nodey4 = doc.createElement('y4')
        nodey4.appendChild(doc.createTextNode(str(box[7])))
        nodebndbox.appendChild(nodey4)
        '''
        # ang = doc.createElement('angle')
        # ang.appendChild(doc.createTextNode(str(angle)))
        # nodebndbox.appendChild(ang)
        nodeobject.appendChild(nodebndbox)
        root.appendChild(nodeobject)
    try:
        fp = open(path + filename, mode='r')
    except FileNotFoundError:
        with open(path + filename, mode='w') as fp:
            doc.writexml(fp, indent='\n', addindent='\t', encoding='UTF-8')
            fp.close()


def load_annoataion(p):
    '''
    load annotation from the text file
    :param p:
    :return:
    '''
    text_polys = []
    text_tags = []
    text_comment = []
    if not os.path.exists(p):
        return np.array(text_polys, dtype=np.float32)
    with open(p, 'r') as f:
        for line in f.readlines()[2:]:
            label = 'text'
            # strip BOM. \ufeff for python3,  \xef\xbb\bf for python2
            #line = [i.strip('\ufeff').strip('\xef\xbb\xbf') for i in line]
            #print(line)

            x1, y1, x2, y2, x3, y3, x4, y4, label, difficult = line.split(' ')[0:10]
            #print(label)
            #print(difficult)

            x1 = float(x1)
            x2 = float(x2)
            x3 = float(x3)
            x4 = float(x4)
            y1 = float(x1)
            y2 = float(y2)
            y3 = float(y3)
            y4 = float(y4)


            xmin = min(min(min(x1, x2), x3), x4)
            ymin = min(min(min(y1, y2), y3), y4)
            xmax = max(max(max(x1, x2), x3), x4)
            ymax = max(max(max(y1, y2), y3), y4)


            if xmin > xmax or ymin > ymax:
                print("wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            text_polys.append([xmin, ymin, xmax, ymax])
            text_tags.append(label)
            text_comment.append(difficult)
            #print(label, difficult)
            #print(text_polys)
        return np.array(text_polys, dtype=np.float32), np.array(text_tags, dtype=np.str), np.array(text_comment, dtype=np.int)

if __name__ == "__main__":
    txt_path = '/home/dingjin/DOTA/train1024/labelTxt/'
    xml_path = '/home/dingjin/DOTA/train1024/dota/DOTA/Annotations/'
    img_path = '/home/dingjin/DOTA/train1024/dota/DOTA/JPEGImages/'
    #print(os.path.exists(txt_path))
    txts = os.listdir(txt_path)
    for count, t in enumerate(txts):
        boxes, labels, difficult = load_annoataion(os.path.join(txt_path, t))
        xml_name = t.replace('.txt', '.xml')
        img_name = t.replace('.txt', '.jpg')
        #print(img_name)
        #print(os.path.join(img_path, img_name))


        img = cv2.imread(os.path.join(img_path, img_name))
        #print(img)

        h, w, d = img.shape
        #print(xml_name, xml_path, boxes, labels, w, h, d)
        WriterXMLFiles(xml_name, xml_path, boxes, labels, difficult, w, h, d)

        if count % 1000 == 0:
            print(count)
