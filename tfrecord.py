import os
def listfileswtotxt(dir, file, wildcard, recursion):
    exts =wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname = os.path.join(dir, name)
        if(os.path.isdir(fullname) & recursion):
            listfileswtotxt(fullname, file, wildcard, recursion)
        else:

            for ext in exts:
                if(name.endswith(ext)):
                    (filename, extension) = os.path.splitext(name)
                    file.write('/home/dingjin/DOTA/trainingsplit416/images/' + filename + '.png' + '\n')
                    break


def Test():
    dir = '/home/dingjin/DOTA/trainingsplit416/images'
    outfile='/home/dingjin/train416.txt'
    wildcard = '.png'

    file = open(outfile,'w+')
    if not file:
        print("cannot open the file %s for writing" % outfile)
    listfileswtotxt(dir, file, wildcard, 1 )

    file.close()


Test()


