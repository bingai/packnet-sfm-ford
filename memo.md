cd packnet-sfm
# Save Models --> Convert pytorch model to torch script via tracing
python3 scripts/jit_trace.py

# if you want to use docker (recommended)
make docker-build

# Infer
python3 scripts/infer.py --checkpoint <checkpoint.ckpt> --input <image or folder> --output <image or folder> [--image_shape <input shape (h,w)>]

## Infer Examples:
### 1. AutoHitch Dataset
**1.1 get the inference for the autohitch image:**\newline
make docker-run COMMAND="python3 scripts/infer.py --checkpoint ./pretrained_models/PackNet01_MR_selfsup_K.ckpt --input ./data/AutoHitch/color_image --output ./data/Autohitch/color_image_output"
