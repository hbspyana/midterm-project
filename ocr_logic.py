import requests
from PIL import Image
from fpdf import FPDF
import pyautogui

# text extractor
def ocr_image(image_path, lang='eng'):
    url = 'https://api.ocr.space/parse/image'
    key = 'K85709985988957'
    try:
        f = open(image_path, 'rb')
        files = {'file': f}
        data = {'language': lang}
        headers = {'apikey': key}

        r = requests.post(url, data=data, files=files, headers=headers)
        f.close()

        result = r.json()
        text = result['ParsedResults'][0]['ParsedText']
        return text
    except:
        return 'Error reading image.'

# save as txt
def save_as_txt(text):
    from tkinter import filedialog, messagebox
    if not text.strip():
        messagebox.showwarning('No text found!', 'Choose an image before saving.')
        return

    # ask user where to save
    filename = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text files', '*.txt')],
        title='Save as TXT'
    )
    with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)


# save as pdf
def save_as_pdf(text):
    from tkinter import filedialog, messagebox
    if not text.strip():
        messagebox.showwarning('No text found!', 'Choose an image before saving.')
        return

    # ask user where to save
    filename = filedialog.asksaveasfilename(
        defaultextension='.pdf',
        filetypes=[('PDF files', '*.pdf')],
        title='Save as PDF'
    )
    if not filename:
        return  # user cancelled

    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)

        # for unsupported chars
        safe_text = text.encode('latin-1', 'replace').decode('latin-1')

        pdf.multi_cell(0, 10, safe_text)
        pdf.output(filename)
        messagebox.showinfo('Saved', f'Text saved as {filename}!')
    except Exception as e:
        messagebox.showerror('Error', f'Could not save PDF:\n{e}')

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
