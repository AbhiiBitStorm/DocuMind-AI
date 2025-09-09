# DocuMind AI 🤖

An AI-powered tool built with Python and Flask to extract, understand, summarize, and translate text from document images using an asynchronous, non-blocking architecture.

## ✨ Key Features

- **Advanced OCR:** Extracts text from images using Tesseract with image preprocessing for better accuracy.
- **NLP Insights:** Identifies key entities (Names, Dates, Organizations) and provides highlighted text visualization.
- **Text Summarization:** Creates concise summaries of long documents using Hugging Face Transformers.
- **Multi-Language Translation:** Translates summaries into multiple languages (Hindi, Marathi, Spanish, etc.).
- **Asynchronous Workflow:** Uses Celery and Redis to process documents in the background, ensuring the UI never freezes.
- **PDF Report Generation:** Allows users to download a well-formatted PDF report of the analysis.
- **REST API:** Includes an API endpoint for programmatic access.

## 🛠️ Technology Stack

- **Backend:** Python, Flask, Celery
- **AI/ML:** PyTesseract, spaCy, Hugging Face Transformers, PyTorch
- **Message Broker:** Redis
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **PDF Generation:** FPDF2

## 🚀 How to Run this Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/DocuMind-AI.git](https://github.com/YourUsername/DocuMind-AI.git)
    cd DocuMind-AI
    ```
2.  **Install all dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ensure Redis is running on your system.**
4.  **Start the Celery worker** (in a new terminal):
    ```bash
    celery -A tasks.celery worker --pool=eventlet --loglevel=info
    ```
5.  **Run the Flask application** (in another new terminal):
    ```bash
    python app.py
    ```
6.  Open your web browser and navigate to `http://127.0.0.1:5000`.