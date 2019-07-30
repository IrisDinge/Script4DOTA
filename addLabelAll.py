import os
import os.path
'''
this code is going to the contect of all .txt in a .txt
output will be found in the same directory just lick filepath

'''

#print('2')
def mergeTxt(filepath, outfile):

    k = open(filepath+outfile, 'a+')
    #print(filepath + outfile)

    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent,filepath)
            f = open(txtPath)
            k.write(f.read())



        k.close()


        print('finished')

if __name__ == "__main__":
    mergeTxt('/labelpath/','annotation.txt')
