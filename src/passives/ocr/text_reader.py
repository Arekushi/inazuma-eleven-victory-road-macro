import pyautogui
import pytesseract
from PIL import ImageOps, ImageEnhance


def read_text_from_screen(
    region: tuple[int, int, int, int],
    language: str = 'por'
) -> str:
    img = pyautogui.screenshot(region=region)    
    img = ImageOps.grayscale(img)
    img = ImageEnhance.Contrast(img).enhance(3.5)
    img = ImageEnhance.Sharpness(img).enhance(2)
    img = img.point(lambda x: 0 if x < 155 else 255, '1')

    text = pytesseract.image_to_string(
        img,
        lang=language,
        config='--psm 6'
    )

    return text


def read_text_from_passive_slot(slot: int = 1):
    return read_text_from_screen(region=(1180, 540 + (85 * (slot - 1)), 650, 75))
