# encoding: utf-8
"""
@author:  Jinkai Zheng
@contact: 1315673509@qq.com
"""

import glob
import os.path as osp
import re
import warnings

from .bases import ImageDataset
from ..datasets import DATASET_REGISTRY


@DATASET_REGISTRY.register()
class PersonX(ImageDataset):
    """PersonX.

    Dataset statistics:
        - identities: 700.
        - images: 20280.
    """

    def __init__(self, root='/home/liuxinchen3/notespace/data/challenge_datasets', **kwargs):

        self.train_dir = osp.join(root, 'personX/image_train')
        self.query_dir = osp.join(root, 'target_validation/image_query')
        self.gallery_dir = osp.join(root, 'target_validation/image_gallery')

        required_files = [
            self.train_dir,
            self.query_dir,
            self.gallery_dir,
        ]
        self.check_before_run(required_files)

        train = self.process_dir(self.train_dir)
        query = self.process_dir(self.query_dir)
        gallery = self.process_dir(self.gallery_dir)

        super(PersonX, self).__init__(train, query, gallery, **kwargs)

    def process_dir(self, dir_path):
        img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
        pattern = re.compile(r'([-\d]+)_c(\d+)')

        data = []
        for img_path in img_paths:
            pid, camid = map(int, pattern.search(img_path).groups())
            # assert 1 <= pid <= 700
            # assert 1 <= camid <= 6
            # camid -= 1  # index starts from 0
            data.append((img_path, pid, camid))

        return data
