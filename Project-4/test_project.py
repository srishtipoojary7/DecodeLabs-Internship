from pathlib import Path
from ocr_engine import preprocess_image

sample = Path("sample_images/sample_text.png")

if not sample.exists():
    raise SystemExit("Sample image is missing.")

_, processed = preprocess_image(str(sample))

if processed is None or processed.size == 0:
    raise SystemExit("Preprocessing failed.")

print("Preprocessing test passed.")
