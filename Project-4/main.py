import argparse
from pathlib import Path

from ocr_engine import run_ocr


def main():
    parser = argparse.ArgumentParser(
        description="Project 4 - Basic Image/Text Recognition using OCR"
    )
    parser.add_argument(
        "--image",
        help="Path to the input image. If omitted, you will be prompted.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Directory for generated output files.",
    )
    args = parser.parse_args()

    image_path = args.image or input("Enter the image path: ").strip().strip('"')

    if not image_path:
        print("No image path supplied.")
        return

    if not Path(image_path).exists():
        print(f"Image not found: {image_path}")
        return

    try:
        text, processed_path, text_path = run_ocr(
            image_path, args.output_dir
        )
    except Exception as exc:
        print("\nERROR:", exc)
        print("\nIf you are on Windows, make sure Tesseract OCR is installed.")
        return

    print("\n========== RECOGNIZED TEXT ==========\n")
    print(text if text else "[No text detected]")
    print("\n======================================")
    print(f"Preprocessed image: {processed_path}")
    print(f"Text output:        {text_path}")


if __name__ == "__main__":
    main()
