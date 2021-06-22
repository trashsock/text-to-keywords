import docx

def ExtractTextFromDocx(filename):
    file_text = getText(filename)
    file_text = file_text.lstrip() # To remove extra spaces before the content
    file_text = file_text.rstrip() # To remove extra spaces after the content
    print("Text in DOCX : ", file_text)
    return file_text

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
