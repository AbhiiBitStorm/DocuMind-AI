from fpdf import FPDF
import os

def create_pdf_report(results, filepath):
    pdf = FPDF()
    pdf.add_page()
    
    # Add a font that supports Unicode (Hindi, Marathi, etc.)
    # Make sure to download this font and place it in your project folder.
    try:
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        font = 'DejaVu'
    except RuntimeError:
        print("Font not found, using Arial. Non-English characters might not render.")
        font = 'Arial'
    
    pdf.set_font(font, 'B', 16)
    pdf.cell(0, 10, 'AI Document Sahayak Report', 0, 1, 'C')
    pdf.ln(10)
    
    pdf.set_font(font, 'B', 12)
    pdf.cell(0, 10, 'Summary', 0, 1)
    pdf.set_font(font, '', 12)
    pdf.multi_cell(0, 10, results['summary'].encode('latin-1', 'replace').decode('latin-1'))
    pdf.ln()

    pdf.set_font(font, 'B', 12)
    pdf.cell(0, 10, 'Translation', 0, 1)
    pdf.set_font(font, '', 12)
    pdf.multi_cell(0, 10, results['translation'])
    pdf.ln()
    
    pdf.set_font(font, 'B', 12)
    pdf.cell(0, 10, 'Key Information', 0, 1)
    pdf.set_font(font, '', 12)
    for entity in results['entities']:
        line = f"- {entity['label']}: {entity['text']}"
        pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'))

    pdf.output(filepath)