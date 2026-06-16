import numpy as np
from PIL import Image
from src.vision.screen import get_ui_scale


def load_template(path: str):
    return Image.open(path).convert('RGB')


def scale_template(img: Image.Image):
    scale = get_ui_scale()

    resized = img.resize(
        (
            int(img.width * scale),
            int(img.height * scale)
        ),
        Image.Resampling.LANCZOS
    )

    return np.array(resized)
