import cv2
import pytesseract
from config import Config

# Set Tesseract command from config
pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_CMD

def preprocess_image(image_path):
    """Improves image quality for better OCR results."""
    img = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to get a binary image
    _, binary_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return binary_img

def extract_text_from_image(image_path):
    try:
        processed_image = preprocess_image(image_path)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        return text
    except Exception as e:
        print(f"OCR Error: {e}")
        return None