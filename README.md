# AMNet: Memorability Estimation with Attention
A PyTorch implementation of our paper [AMNet: Memorability Estimation with Attention](https://arxiv.org/abs/1804.03115)
by Jiri Fajtl, Vasileios Argyriou, Dorothy Monekosso and Paolo Remagnino. This paper will be presented 
at [CVPR 2018](http://cvpr2018.thecvf.com/).
 
==> [AMNet](https://github.com/ok1zjf/AMNet)  
  
# Server Path
服务器文件路径：
/media/Data/qipeng/modified_complete_images
/home/qipeng/PicMemorability/AMNet-Rumor

Train Cmd
python3.5 main.py --train-batch-size 222 --test-batch-size 222 --cnn ResNet50FC --dataset lamem --dataset-root /media/Data/qipeng/modified_complete_images/pre_handle_add_label/lamem/ --train-split train_1 --val-split val_1

Test Cmd
python3.5 main.py --test --dataset lamem --dataset-root /media/Data/qipeng/modified_complete_images/pre_handle_add_label/lamem/ --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --test-split 'test_*'

Predict Cmd - Rumor / Nonrumor
python3.5 main.py --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --eval-images /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/images/rumor --csv-out memorabilities-rumor.txt --att-maps-out /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/att_maps/rumor
python3.5 main.py --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --eval-images /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/images/nonrumor --csv-out memorabilities-nonrumor.txt --att-maps-out /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/att_maps/nonrumor

Predict Cmd - Sample
python3.5 main.py --cnn ResNet50FC --model-weights /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Train-Output/lamem_ResNet50FC_lstm3_train_1/weights_54.pkl --eval-images /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/images/sample --csv-out memorabilities-sample.txt --att-maps-out /media/Data/qipeng/modified_complete_images/pre_handle_add_label/AMNet-Predict/att_maps/sample

# Client Path