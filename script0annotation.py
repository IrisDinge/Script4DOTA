import os

emptynamelistohne=[]

def clearafterspilt(labelTxtpath):

    '''

    :param path: the directory of files folder which is going to be searched
    :return: the list of all empty files
    '''

    files = os.listdir(labelTxtpath)
    for file in files:
        txt_path = os.path.join(labelTxtpath, file)


        if os.path.getsize(txt_path) == 0:
            print(txt_path, "empty")                                      #FLAG: important
            split_name = os.path.splitext(os.path.basename(txt_path))[0]  #only the name of empty files
            emptynamelistohne.append(split_name)                          #save into a list
            #emptynamelist.append(txt_path)   #get the name of empty file
            os.remove(txt_path)  # delete the empty annotation

    for i in emptynamelistohne:

        name = '/home/dingjin/DOTA/val_416_no_empty/images/' + i + '.png'
        os.path.normpath(name)
        print(name)
        os.remove(name) #delete the image


    #print(emptynamelistohne)

#print("ready to go next")

if __name__ == "__main__":
    clearafterspilt('/home/dingjin/DOTA/val_416_no_empty/labelTxt/')