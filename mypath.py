class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            return '/content/VOCdevkit/VOC2012'  # folder that contains VOCdevkit/.
        elif dataset == 'sbd':
            return '/content/benchmark_RELEASE'  # folder that contains dataset/.
        elif dataset == 'cityscapes':
            return '/path/to/datasets/cityscapes/'     # foler that contains leftImg8bit/
        elif dataset == 'coco':
            return '/content/gconv-pytorch-deeplab-xception'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError
