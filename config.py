import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = 'uploads'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    # Optional: Path to Tesseract executable
    TESSERACT_CMD = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'