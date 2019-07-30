import os
'''
this script is going to create a .txt for <imagepath> <box1> <box2> etc.

'''

def transyolo2kerasyolo(labelpath, imagepath):
    name = []
    files = os.listdir(labelpath)
    s=[]
    for file in files:
        txt_path = os.path.join(labelpath,file)
        #print(file)
        if not os.path.isdir(file):
            #if os.path.getsize(txt_path) != 0:
                #print(txt_path)

            f = open(labelpath + file);
            iter_f = iter(f);
            name = os.path.splitext(os.path.basename(txt_path))[0]
            #print(name)
            str = imagepath  + name + '.png' + ' '
            for line in iter_f:
                str = str + line

        s.append(str)
        dj = '\n'.join(s)
        print(dj)
        file = open('/home/dingjin/tra_val_416.txt','w')
        file.write(dj)
        file.close()

if __name__ == "__main__":
    transyolo2kerasyolo('/data/tmp/dingjin2daniel/DOTA/416/new_tra+val_416/label/',
                        '/data/tmp/dingjin2daniel/DOTA/416/new_tra+val_416/images/')
