from os import chdir
import imageio
from utils.utils import chdir_to_file_dir

chdir_to_file_dir(__file__)

color_resources = [
    "ch4/resource/red.png",    
    "ch4/resource/green.png",    
    "ch4/resource/green_2.png",    
    "ch4/resource/blue.png",    
]

for img_path in color_resources:

    # red_img = imageio.imread("ch4/resource/red.png")
    print("current image path is: {}".format(img_path))
    
    # 方法1 使用 imageio
    # img = imageio.imread(img_path)
    
    # 方法2 使用 PIL
    from PIL import Image
    import numpy as np
    img = np.asarray(Image.open(img_path))
    
    # W【宽】H【高】C【红绿蓝通道】
    # print("red_img shape: {}".format(img.shape))

    import torch
    img_tensor = torch.from_numpy(img)
    img_tensor_out = img_tensor.permute(2, 0, 1)
    img_tensor_out = img_tensor_out.float()
    # print("red out: {} shape: {}".format(img_tensor_out, img_tensor_out.shape))

    print(torch.mean(img_tensor_out[0]))
    print(torch.mean(img_tensor_out[1]))
    print(torch.mean(img_tensor_out[2]))
