# encoding:utf-8

import os

# Path of Files
path = os.getcwd()
src_path = path + '/source'
des_path = path + '/output'
train_out_file = des_path + '/train.txt'
# val_out_file = des_path + '/val.txt'

train_out = open(train_out_file, 'w')
# val_out = open(val_out_file, 'w')

for root, dirs, files in os.walk(src_path, topdown=False):
    for name in files:
        # 判断是否是图片文件
        # if '.jpg' not in name:
        #     continue
        if 'train' in root:
            if 'nonrumor' in root:
                train_out.write(name + ' 0\n')
            else:
                train_out.write(name + ' 1\n')
        # if 'validation' in root:
        #     if 'nonrumor' in root:
        #         val_out.write(name + ' 0\n')
        #     else:
        #         val_out.write(name + ' 1\n')

train_out.close()
# val_out.close()

# 服务器地址：10.25.0.232 用户名：qipeng 密码：senochow
# 服务器文件路径：
# /media/Data/qipeng/modified_complete_images
# /home/qipeng/PicMemorability/AMNet-Rumor

# Train Cmd
# python3.5 main.py --train-batch-size 222 --test-batch-size 222 --cnn ResNet50FC --dataset lamem --dataset-root /media/Data/qipeng/modified_complete_images/pre_handle_add_label/lamem/ --train-split train_1 --val-split val_1

# Test Cmd
# python3.5 main.py --test --dataset lamem --dataset-root /media/Data/qipeng/modified_complete_images/pre_handle_add_label/lamem/ --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --test-split 'test_*'
#
# Predict Cmd - Rumor / Nonrumor
# python3.5 main.py --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --eval-images /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/images/rumor --csv-out memorabilities-rumor.txt --att-maps-out /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/att_maps/rumor
# python3.5 main.py --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --eval-images /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/images/nonrumor --csv-out memorabilities-nonrumor.txt --att-maps-out /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/att_maps/nonrumor
#
# Predict Cmd - Sample
# python3.5 main.py --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --eval-images /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/images/sample --csv-out memorabilities-sample.txt --att-maps-out /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/att_maps/sample
