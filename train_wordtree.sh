export CUDA_VISIBLE_DEVICES=0
python -m paddle.distributed.launch --gpus="0" tools/train.py -c ./ppcls/configs/ImageNet/MobileNetV2/MobileNeyV2_wordtree.yaml