#import magic
import os
import filetype

from progressbar import ProgressBar
 
path ='D:\\DeepLearning\\Matrix-Capsules-EM-Tensorflow-master\\data\\nyu2_train'
 
original_images =[]
 
for root, dirs, filenames in os.walk(path):
 
    for filename in filenames:
 
        original_images.append(os.path.join(root, filename))
 
original_images = sorted(original_images)

progress = ProgressBar()
for filename in progress(original_images):
        if filename.endswith('jpeg') or filename.endswith('png'):
            # a = magic.from_file(pic_file,mime=True )
            # print(pic_file, a)
            kind = filetype.guess(filename)
            getExt = str(kind.mime).split('/')[1]
            #print(pic_file, kind.extension, kind.mime)
            mainName, ext = os.path.splitext(filename)
            ext = ext[1:]
            if ext != getExt:
                # if(getExt != 'jpeg' and getExt != 'png'):
                #     os.remove(pic_file)
                print(filename, getExt)
                os.renames(filename, mainName + "." + getExt)