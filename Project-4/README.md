# Artificial Intelligence – Project 4
## Basic Image/Text Recognition using OCR

This project implements **Path 1: Optical Character Recognition (OCR)** from the DecodeLabs Project 4 brief.

### What the project does
1. Reads an input image.
2. Converts it to grayscale.
3. Applies Gaussian blur to reduce noise.
4. Applies adaptive thresholding to improve character contrast.
5. Uses **pytesseract (Tesseract OCR)** to recognize text.
6. Displays the recognized text and saves the preprocessed image and text output.

### Project structure
```text
AI_Project_4_OCR/
├── main.py
├── ocr_engine.py
├── requirements.txt
├── run_ocr.bat
├── README.md
├── sample_images/
│   └── sample_text.png
└── outputs/
```

## Requirements
- Python 3.9 or newer
- Tesseract OCR
- Python packages in `requirements.txt`

### Windows – install Tesseract
Install Tesseract OCR and make sure `tesseract.exe` is available in PATH.

If it is installed in the common Windows location but not in PATH, the program automatically checks:
`C:\Program Files\Tesseract-OCR\tesseract.exe`

## Install Python packages
Open PowerShell/Command Prompt inside this folder:

```powershell
python -m pip install -r requirements.txt
```

## Run the project

### Easiest method
Double-click `run_ocr.bat`, then enter the image path when prompted.

### Command line
```powershell
python main.py --image sample_images/sample_text.png
```

The output is saved in:
```text
outputs/recognized_text.txt
outputs/preprocessed.png
```

You can also specify an output directory:
```powershell
python main.py --image sample_images/sample_text.png --output-dir outputs
```

## Expected sample output
The included sample image contains a short paragraph. The program should recognize text similar to:

```text
ARTIFICIAL INTELLIGENCE
Project 4 - OCR Demo
Machine learning helps computers understand information.
Optical Character Recognition converts text in an image into editable text.
```

Small differences in OCR output can occur depending on the Tesseract version and image quality.

## Pre-processing pipeline
```text
Input Image
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Adaptive Thresholding
     ↓
Tesseract OCR
     ↓
Recognized Text
```

## Why this satisfies Project 4
The project uses a pre-trained recognition library instead of training a model from scratch. It demonstrates model/library integration, image preprocessing, text recognition, and displaying/saving the model output.
