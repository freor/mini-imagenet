import os
import subprocess
from tqdm import tqdm
import subprocess


def img_name_convert(mini_img_path):
    '''
    SPEC
        > convert original name to new "0" added name
        > and put new directory without label's directory
    '''
    mini_img_path = "./dataset/new_dataset/"

    # list of files in "mini_img_path"
    files = os.listdir(mini_img_path)

    for f in tqdm(files):
        path = mini_img_path + f + "/"
        images = os.listdir(path) # list of images in each directory

        for i in images:
            t = i.split('_')

            img_name = []
            img_name += [t[0]]

            ext = t[1].split('.')
            img_name += [ext[0]]
            ext = ext[1]

            num_len = len(img_name[1])
            count = 8 - num_len
            tmp = img_name[1]
            for _ in range(count):
                tmp = "0" + tmp

            img = img_name[0] + tmp + "." + ext

            tmp = os.system("mv %s %s" % (path + i, path + img))

    print("file names of new mini-imagenet dataset are successfully changed!")

def move_images(path):
    sp_cmd = ['/bin/bash', '-c']

    img_path = path
    dirts = os.listdir(path)

    for d in tqdm(dirts):
        #res = os.system("mv %s ../" % (path + d + "/*"))
        print(path+d)
        #res = os.system("rm -rf %s" % (path + d))
        t = subprocess.Popen(sp_cmd + ["mv %s %s" % (path + d + '/*', path)],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        t.communicate()
        t = subprocess.Popen(sp_cmd + ["rm -rf %s" % (path + d)],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        t.communicate()



    print("all files are moved to '../' successfully")


if __name__ == "__main__":
    origin_path = "./dataset/new_dataset/"

    #img_name_convert(origin_path)
    move_images(origin_path)


