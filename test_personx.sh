gpus='2'

CUDA_VISIBLE_DEVICES=$gpus python tools/train_net.py --config-file 'projects/StrongerBaseline/configs/sbs_personx.yml' --eval-only MODEL.WEIGHTS /home/liuxinchen3/zhengjinkai/fast-reid/fast-reid_20200430/projects/StrongerBaseline/logs/visda20/sbs_personx_market1501/model_final.pth