

import os
from PIL import Image 

for path in os.listdir("orchid_style/images"):
    im = Image.open("orchid_style/images/" + path)
    im1 = im.crop((66, 47, 460, 341))
    # im1 = im.crop((66, 25, 460, 164))
    im1 = im1.save("orchid_style/images/" + path)