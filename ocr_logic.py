import requests
from fpdf import FPDF
from tkinter import filedialog, messagebox

# text extractor
def ocr_image(image_path, lang='eng'):
    url = 'https://api.ocr.space/parse/image'
    key = 'K85709985988957'
    try:
        f = open(image_path, 'rb') # 'rb' = 'read binary' mode; images are binary data
        files = {'file': f}
        data = {'language': lang}
        headers = {'apikey': key}

        r = requests.post(url, data=data, files=files, headers=headers) # sends above to url
        f.close()

        result = r.json() # url sends back text
        text = result['ParsedResults'][0]['ParsedText'] # extracts text from result
        return text
    except:
        return 'Error reading image.'

# save as txt
def save_as_txt(text):
    if not text.strip():
        messagebox.showwarning('No text found!', 'Choose an image before saving.')
        return

    filename = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text files', '*.txt')],
        title='Save as TXT'
    )
    with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)


# save as pdf
def save_as_pdf(text):
    if not text.strip():
        messagebox.showwarning('No text found!', 'Choose an image before saving.')
        return

    filename = filedialog.asksaveasfilename(
        defaultextension='.pdf',
        filetypes=[('PDF files', '*.pdf')],
        title='Save as PDF'
    )
    if not filename:
        return  # cancel

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    safe_text = text.encode('latin-1', 'replace').decode('latin-1') # for unsupported chars

    pdf.multi_cell(0, 10, safe_text)
    pdf.output(filename)

# log
def write_log(text):
    f = open('log.txt', 'a', encoding='utf-8')
    f.write(text + '\n')
    f.close()

def read_log():
    try:
        f = open('log.txt', 'r', encoding='utf-8')
        content = f.read()
        f.close()
        return content
    except:
        return 'Log file not found'
