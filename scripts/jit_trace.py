# Copyright 2020 Toyota Research Institute.  All rights reserved.

# import numpy as np
# import os
import torch

# from glob import glob
# from cv2 import imwrite

from packnet_sfm.models.model_wrapper import ModelWrapper
from packnet_sfm.datasets.augmentations import resize_image, to_tensor
from packnet_sfm.utils.horovod import hvd_init, rank, world_size, print0
from packnet_sfm.utils.image import load_image
from packnet_sfm.utils.config import parse_test_file
# from packnet_sfm.utils.load import set_debug
# from packnet_sfm.utils.depth import write_depth, inv2depth, viz_inv_depth
# from packnet_sfm.utils.logging import pcolor


def main():
    
    # Initialize horovod
    hvd_init()

    # ckpt_file = './pretrained_models/vp_rear_fisheye_K_4_03_15_2021.ckpt'
    ckpt_file = './pretrained_models/vp_rear_pinhole_K_40_03_15_2021.ckpt'

    # Parse arguments
    config, state_dict = parse_test_file(ckpt_file)

    # If no image shape is provided, use the checkpoint one 
    image_shape = config.datasets.augmentation.image_shape

    # Initialize model wrapper from checkpoint arguments
    model_wrapper = ModelWrapper(config, None, None, load_datasets=False)
    
    # Restore monodepth_model state
    model_wrapper.load_state_dict(state_dict)

    # # change to half precision for evaluation if requested
    # dtype = torch.float16 if args.half else None

    # # Send model to GPU if available
    # if torch.cuda.is_available():
    #     # model_wrapper = model_wrapper.to('cuda:{}'.format(rank()), dtype=dtype)

    # Set to eval mode
    model_wrapper.eval()

    # Input image
    input_image = load_image('./data/datasets/ValetParking/input_image.png')

    # Resize Input image to the predefined image shape
    input_image_resized = resize_image(input_image, image_shape)
    input_image_resized = to_tensor(input_image_resized).unsqueeze(0)

    model = model_wrapper.model.depth_net
    model.eval()

    traced_script_module = torch.jit.trace(model, input_image_resized)
    # traced_script_module.save('./traced_model_pt/vp_rear_fisheye_K_4_03_15_2021.pt')
    traced_script_module.save('./traced_model_pt/vp_rear_pinhole_K_40_03_15_2021.pt')

if __name__ == '__main__':
    main()
