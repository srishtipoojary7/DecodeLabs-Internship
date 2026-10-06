import os
from pathlib import Path

import cv2
import numpy as np
import pytesseract


def configure_tesseract():
    """Use Tesseract from PATH, or the common Windows installation path."""
    try:
        pytesseract.get_tesseract_version()
        return
    except Exception:
        windows_path = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
        if windows_path.exists():
            pytesseract.pytesseract.tesseract_cmd = str(windows_path)
        else:
            raise RuntimeError(
                "Tesseract OCR was not found. Install Tesseract and add it to PATH."
            )


def preprocess_image(image_path: str):
    """Apply the preprocessing pipeline specified for the OCR path."""
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresholded = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2,
    )
    return image, thresholded


def recognize_text(processed_image):
    """Run the pre-trained Tesseract OCR engine."""
    config = "--oem 3 --psm 6"
    text = pytesseract.image_to_string(processed_image, config=config)
    return text.strip()


def run_ocr(image_path: str, output_dir: str = "outputs"):
    configure_tesseract()

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    _, processed = preprocess_image(image_path)
    text = recognize_text(processed)

    processed_path = output / "preprocessed.png"
    text_path = output / "recognized_text.txt"

    cv2.imwrite(str(processed_path), processed)
    text_path.write_text(text + "\n", encoding="utf-8")

    return text, processed_path, text_path
