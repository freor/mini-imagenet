from data_generator import *
from rn_mnimagenet import *
from make_csv import *


new_path = "./dataset/new_dataset/"
csv_path = "./dataset/"
final_path = "./dataset/new_dataset/"

# make new mini imagenet dataset
print("1. Making new mini-imagenet dataset!")
data_generator()
# change file name with "0" added
print("2. Img Name is being converted...")
img_name_convert(new_path)
# make csv file for train, val and test
print("3. CSV file is being made...")
make_tvt_csv(new_path, csv_path)
# make new final dataset by moving imgs into one directory
print("4. new final dataset is being made...!")
move_images(final_path)








