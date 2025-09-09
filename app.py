import os
from flask import Flask, request, render_template, redirect, url_for, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from config import Config
from tasks import celery, process_document_task

app = Flask(__name__)
app.config.from_object(Config)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file selected. Please choose an image.")
        file = request.files['file']
        if file.filename == '' or not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return render_template('index.html', error="Invalid file type. Please upload a PNG or JPG image.")
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        language = request.form.get('language', 'hi')
        task = process_document_task.delay(filepath, language)
        
        # We pass only the filename, not the full path
        return redirect(url_for('result', task_id=task.id, filename=filename))
        
    return render_template('index.html')

@app.route('/result/<task_id>/<filename>')
def result(task_id, filename):
    return render_template('result.html', task_id=task_id, filename=filename)

@app.route('/status/<task_id>')
def task_status(task_id):
    task = celery.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {'state': 'PENDING', 'status': 'Waiting for worker...'}
    elif task.state == 'SUCCESS':
        response = {'state': 'SUCCESS', 'result': task.info}
    else: #FAILURE
        response = {'state': 'FAILURE', 'status': str(task.info)}
    return jsonify(response)

# --- YEH NAYA ROUTE ADD KIYA GAYA HAI ---
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serves the uploaded image file to the browser."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
# ----------------------------------------

# Note: PDF download functionality can be added back here if needed
# Just make sure to pass the results to the PDF module correctly

if __name__ == '__main__':
    app.run(debug=True)