##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil



def moveFile(fileDir):
    pathimageDir = os.listdir(fileDir)
    pathlabelDir = os.listdir((labelfileDir))

    imagesfilenumber = len(pathimageDir)
    rate = 0.5
    imagespicknumber = int(imagesfilenumber * rate)
    imagessample = random.sample(pathimageDir, imagespicknumber)

    #print(imagessample)


    for imagename in imagessample:

        labelname = os.path.splitext(imagename)[0] + '.txt'

        shutil.move(fileDir + imagename, tarDir + imagename)
        #os.remove(fileDir + imagename)
        shutil.move(labelfileDir + labelname, labeltarDir + labelname)
        #os.remove(labelfileDir + labelname)


        #shutil.rmtree(fileDir + imagename)
        #shutil.rmtree(labelfileDir + labelname)
    return


if __name__ == "__main__":
    fileDir = '/home/dingjin/DOTA/DOTA/images/'  # original path
    tarDir = '/home/dingjin/splittest/images/'  # new path
    labelfileDir = '/home/dingjin/DOTA/DOTA/labelTxt/' #labelTxt
    labeltarDir = '/home/dingjin/splittest/labelTxt/'
    moveFile(fileDir)
















