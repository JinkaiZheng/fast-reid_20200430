gpus='2,3'

CUDA_VISIBLE_DEVICES=$gpus python train_net.py --config-file 'configs/sbs_personx.yml'