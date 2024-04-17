#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2024/4/17 11:00
# @Author : ClipT
# @File : split_data.py
# @Software: PyCharm
# @Note:
import os, shutil
import random


def mymovefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("src not exist!")
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.move(srcfile, dstfile)  # 移动文件


test_rate = 0.2  # 训练集和测试集的比例为8:2。
img_num = 12500  # 猫和狗分别都是12500张
test_num = int(img_num * test_rate)

test_index = random.sample(range(0, img_num), test_num)
# print(test_index)
file_path = r"D:\pythonProject\Classic_model_examples\2015_ResNet18_MNIST\data\kagglecatsanddogs_5340\PetImages"
tr = "train"
te = "validation"
cat = "cat"
dog = "dog"

# 将上述index中的文件都移动到/test/Cat/和/test/Dog/下面去。
for i in range(len(test_index)):
    # 移动猫
    srcfile = os.path.join(file_path, tr, cat, str(test_index[i]) + ".jpg")
    # print(srcfile)
    dstfile = os.path.join(file_path, te, cat, str(test_index[i]) + ".jpg")
    mymovefile(srcfile, dstfile)
    # 移动狗
    srcfile = os.path.join(file_path, tr, dog, str(test_index[i]) + ".jpg")
    # print(srcfile)
    dstfile = os.path.join(file_path, te, dog, str(test_index[i]) + ".jpg")
    mymovefile(srcfile, dstfile)