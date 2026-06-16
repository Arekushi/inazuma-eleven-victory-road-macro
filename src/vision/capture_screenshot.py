import mss
import numpy as np
from PIL import Image
from src.vision.dataclasses import Region


def capture_screenshot(
    region: Region,
    save_image = False
):
    x, y, width, height = region

    with mss.mss() as sct:
        monitor = {
            'left': x,
            'top': y,
            'width': width,
            'height': height
        }

        img = np.array(sct.grab(monitor))
        
        if save_image:
            Image.fromarray(img).save('test.png')
        
        return img
