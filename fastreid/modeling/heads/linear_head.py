# encoding: utf-8
"""
@author:  liaoxingyu
@contact: sherlockliao01@gmail.com
"""

from .build import REID_HEADS_REGISTRY
from ...layers import *


@REID_HEADS_REGISTRY.register()
class LinearHead(nn.Module):
    def __init__(self, cfg, in_feat, num_classes, pool_layer=nn.AdaptiveAvgPool2d(1)):
        super().__init__()

        self.pool_layer = nn.Sequential(
            pool_layer,
            Flatten()
        )

        # identity classification layer
        if cfg.MODEL.HEADS.CLS_LAYER == 'linear':
            self.classifier = nn.Linear(in_feat, num_classes, bias=False)
        elif cfg.MODEL.HEADS.CLS_LAYER == 'arcface':
            self.classifier = Arcface(cfg, in_feat)
        elif cfg.MODEL.HEADS.CLS_LAYER == 'circle':
            self.classifier = Circle(cfg, in_feat)
        else:
            self.classifier = nn.Linear(in_feat, num_classes, bias=False)

    def forward(self, features, targets=None):
        """
        See :class:`ReIDHeads.forward`.
        """
        global_feat = self.pool_layer(features)
        if not self.training:
            return global_feat
        # training
        try:
            pred_class_logits = self.classifier(global_feat)
        except TypeError:
            pred_class_logits = self.classifier(global_feat, targets)
        return pred_class_logits, global_feat, targets
