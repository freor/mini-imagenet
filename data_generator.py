import os
import sys
import subprocess
#import glob

base = "./dataset/data_tar/"
IMAGE_NET_DATA1 = base + "ILSVRC2012_img_train.tar"
IMAGE_NET_DATA2 = base + "ILSVRC2012_img_train_t3.tar"

imagenet_path = "./mini_imagenet.txt" # file name path
dir_path = "./dataset/data_tar/" # Imagenet dataset path
tmp_img_path = "./dataset/data_tmp/" # temporal directory for mini-Imagenet datas
new_img_path = "./dataset/new_dataset/" # directory for new dataset: mini-Imagenet
file_format = ".tar"

NUM_CLASS = 100
NUM_EXMP = 600
NUM_STRIDE = NUM_EXMP + 2 # 2 is for "file name" and "'\n'"

sp_cmd = ['/bin/bash', '-c']

# directory setup
# if not exist, create dir

if os.path.exists(tmp_img_path):
    print("Removing existing file and Creating %s" % tmp_img_path)
    t = subprocess.Popen(sp_cmd + ["rm -rf %s" % tmp_img_path],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
    t.communicate()
    t = subprocess.Popen(sp_cmd + ["mkdir %s" % tmp_img_path],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
    t.communicate()
else:
    print("Creating %s" % tmp_img_path)
    t = subprocess.Popen(sp_cmd + ["mkdir %s" % tmp_img_path],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
    t.communicate()

if os.path.exists(new_img_path):
    print("Removing existing file and Creating %s" % new_img_path)
    t = subprocess.Popen(sp_cmd + ["rm -rf %s" % new_img_path],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
    t.communicate()
    t = subprocess.Popen(sp_cmd + ["mkdir %s" % new_img_path],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
    t.communicate()
else:
    print("Creating %s" % new_img_path)
    t = subprocess.Popen(sp_cmd + ["mkdir %s" % new_img_path],
                                                 stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE)
    t.communicate()


# ILSVR unzip
print("Unzipping %s and %s" % (IMAGE_NET_DATA1, IMAGE_NET_DATA2))
cmd = "tar -xvf %s -C %s & tar xvzf %s -C %s" % (IMAGE_NET_DATA1, tmp_img_path, IMAGE_NET_DATA2, tmp_img_path)
t = subprocess.Popen(sp_cmd + [cmd],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
t.communicate()

'''
# exact directory of temporal images
img_dir = os.path.dirname(tmp_img_path)
'''

# make DICT for imagenet_path
print("Making DICTIONARY for Imagenet")
fn_txt = open(imagenet_path, "r")
fn_split = fn_txt.read().split("\n")

img_dict = {}
for i in range(NUM_CLASS):
    img_dict[fn_split[i * NUM_STRIDE]] = fn_split[i * NUM_STRIDE + 1: i * NUM_STRIDE + NUM_EXMP + 1]

for key, value in img_dict.items():
    img_num = key.split('/')[3]
    img_fn =  tmp_img_path + img_num + file_format # e.g. "/dataset/data_tmp/n01614925.tar"
    print("Unzipping %s" % img_fn)
    try:
        t = subprocess.Popen(sp_cmd + ["tar -xvf %s -C %s" % (img_fn, tmp_img_path)],
                                                     stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
        t.communicate()
    except:
        print("ERROR: No file exists.")
        sys.exit(0)

    #imgs_path = dir_path + img_num + "/"

    npath = new_img_path + img_num

    # create directory "./dataset/new_dataset/n01614925"
    if os.path.exists(npath):
        print("Creating %s" % npath)
        t = subprocess.Popen(sp_cmd + ["rm -rf %s" % npath],
                                                     stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
        t.communicate()
    else:
        print("Creating %s" % npath)
        t = subprocess.Popen(sp_cmd + ["mkdir %s" % npath],
                                                     stdout=subprocess.PIPE,
                                                     stderr=subprocess.PIPE)
        t.communicate()

    npath += "/"

    for n in value:
        tmp_nimg = tmp_img_path + n#imgs_path + n
        print("%s is processed" % tmp_nimg)
        try:
            t = subprocess.Popen(sp_cmd + ["mv %s %s" % (tmp_nimg, npath)],
                                                         stdout=subprocess.PIPE,
                                                         stderr=subprocess.PIPE)
            t.communicate()
        except:
            print("ERROR: No file exists.")
            sys.exit(0)

print("Removing created %s" % tmp_img_path)
t = subprocess.Popen(sp_cmd + ["rm -rf %s" % tmp_img_path],
                                             stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
t.communicate()

print("mini-Imagenet created successfully!")

