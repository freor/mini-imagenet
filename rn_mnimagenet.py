import os
import subprocess


def img_name_convert(mini_img_path, new_img_path):
    mini_img_path = "./dataset/new_dataset/"
    new_img_path = "./dataset/rn_mn_img/"

    if os.path.exists(new_img_path):
        tmp = os.system("rm -rf %s" % new_img_path)
    tmp = os.system("mkdir %s" % new_img_path)

    # list of files in "mini_img_path"
    files = os.listdir(mini_img_path)

    for f in files:
        path = mini_img_path + f + "/"
        images = os.listdir(path) # list of images in each directory

        for i in images:
            t = i.split('_')

            img_name = []
            img_name += [t[0]]
            print(img_name)

            ext = t[1].split('.')
            img_name += [ext[0]]
            ext = ext[1]

            num_len = len(img_name[1])
            count = 8 - num_len
            tmp = img_name[1]
            for _ in range(count):
                tmp = "0" + tmp

            img = img_name[0] + tmp + "." + ext

            tmp = os.system("cp %s %s" % (path + i, new_img_path + img))

    print("new mini-imagenet dataset for 'Relation Network for Few-Shot Learning' is successfully created.")

if __name__ == "__main__":
    origin_path = "./dataset/new_dataset/"
    new_path = "./dataset/rn_mn_img/"

    img_name_convert(origin_path, new_path)





