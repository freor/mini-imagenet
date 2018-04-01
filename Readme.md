# Mini Imagenet Dataset Creater
> reference to [Matching Network](https://arxiv.org/pdf/1606.04080.pdf)

> can be used for training [Learning to Compare: Code/Github](https://github.com/dragen1860/LearningToCompare-Pytorch)

## Usage

download Imagenet dataset in `./dataset/data_tar`

| dataset

| | - data_tar

| | | - ILSVRC2012_img_trian.tar

| | | - ILSVRC2012_img_train_t3.tar


`python3 main.py`

## Specification

> `mini_imagenet.txt` for list of files in Imagenet dataset; from ![Matching Network](https://arxiv.org/pdf/1606.04080.pdf)

> `data_generator.py` for unzipping Imagenet dataset

> `rn_mnimagenet.py` for changing the name of files and moving files

> `make_csv` for making train / validation / test file list in csv format

