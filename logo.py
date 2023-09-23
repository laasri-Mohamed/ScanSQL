import random
import base64
from termcolor import colored

logolist = ["ICBfX19fX19fX18gICAgICAgICAgICAgICAgICAgICAgICAgIF9fX19fX19fX19fX19fX19fICAgLl9fX18gICAgICAKIC8gICBfX19fXy8gIF9fX18gIF9fX19fICAgICBfX19fICAgLyAgIF9fX19fL1xfX19fXyAgXCAgfCAgICB8ICAgICAKIFxfX19fXyAgXCBfLyBfX19cIFxfXyAgXCAgIC8gICAgXCAgXF9fX19fICBcICAvICAvIFwgIFwgfCAgICB8ICAgICAKIC8gICAgICAgIFxcICBcX19fICAvIF9fIFxffCAgIHwgIFwgLyAgICAgICAgXC8gICBcXy8uICBcfCAgICB8X19fICAKL19fX19fX18gIC8gXF9fXyAgPihfX19fICAvfF9fX3wgIC8vX19fX19fXyAgL1xfX19fX1wgXF8vfF9fX19fX18gXCAKICAgICAgICBcLyAgICAgIFwvICAgICAgXC8gICAgICBcLyAgICAgICAgIFwvICAgICAgICBcX18+ICAgICAgICBcLyA="]

def chooselogo():
    contact = ""
    if random.randint(1, 100) > 90:
        if random.randint(1, 1000000) == 1:
            return base64.b64decode(logolist[len(logolist) - 1]) + contact
        else:
            return base64.b64decode(logolist[random.randint(1, len(logolist) - 2)]) + contact
    else:
        return base64.b64decode(logolist[0]).decode('utf-8') + contact