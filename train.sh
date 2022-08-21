#!/usr/bin/env bash

# for single card train
# python3.7 tools/train.py -c ./ppcls/configs/ImageNet/ResNet/ResNet50.yaml

# for multi-cards train
# export CUDA_VISIBLE_DEVICES=0
# python -m paddle.distributed.launch --gpus="0" tools/train.py -c ./ppcls/configs/ImageNet/MobileNetV2/MobileNetV2.yaml
export CUDA_VISIBLE_DEVICES=0
python -m paddle.distributed.launch --gpus="0" tools/train.py -c ./ppcls/configs/ImageNet/MobileNetV2_CBAM/MobileNetV2_CBAM_fourclass.yaml