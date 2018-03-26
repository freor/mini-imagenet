import csv
import os
import numpy as np


def make_tvt_csv(p, csv_path):
    '''
    SPEC
       > 64 classes for train
       > 16 classes for val
       > 20 classes for test
       > "tvt" stands for "train validation test"
    INPUT
       >  p: path for mini-imagenet dataset
       >  csv_path: directory path for csv files
    OUTPUT
       >  train.csv, val.csv, test.csv
    '''
    NTRAIN, NVAL, NTEST = 64, 16, 20
    assert (NTRAIN + NVAL + NTEST == 100)


    labels = os.listdir(p) # ["n01614925", "n02071294", ...]
    ncls = len(labels) # the number of classes
    nums = np.random.permutation(ncls).tolist()

    train, val, test = nums[0:NTRAIN], nums[NTRAIN: NTRAIN + NVAL], nums[-NTEST:]
    assert (len(train) + len(val) + len(test) == 100)

    # make "train.csv"
    print("Making 'train.csv'...")
    output = open(csv_path + "train.csv", "w")
    writer = csv.writer(output)

    for l in train:
        v = p + labels[l]
        fs = os.listdir(v)

        for f in fs:
            writer.writerow([f, labels[l]])

    # make "val.csv"
    print("Making 'val.csv'...")
    output = open(csv_path + "val.csv", "w")
    writer = csv.writer(output)

    for l in val:
        v = p + labels[l]
        fs = os.listdir(v)

        for f in fs:
            writer.writerow([f, labels[l]])

    # make "test.csv"
    print("Making 'test.csv'...")
    output = open(csv_path + "test.csv", "w")
    writer = csv.writer(output)

    for l in test:
        v = p + labels[l]
        fs = os.listdir(v)

        for f in fs:
            writer.writerow([f, labels[l]])

    print("'train.csv', 'val.csv' and 'test.csv' is successfully created!!")


if __name__ == '__main__':
    path = "./dataset/new_dataset/"
    csv_path = "../RelationNetworkFewShot/"
    make_tvt_csv(path, csv_path)

