from io import StringIO
from werkzeug.utils import secure_filename
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import requests
from requests.auth import HTTPBasicAuth
import json
from pathlib import Path

def ExtractTextFromPDF(filename):
    output_string = StringIO()
    file_data = ""

    with open(filename, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        # print(output_string.getvalue())
        output_string.seek(0) # Move to the beginning of the text
        file_data = output_string.read() # Read the entire text and store it into a string
        file_data = file_data.lstrip() # To remove extra spaces before the content
        file_data = file_data.rstrip() # To remove extra spaces after the content
        # print("Text In PDF File : ", file_data)

    return file_data


