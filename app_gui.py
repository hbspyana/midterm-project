import tkinter as tk
from tkinter import filedialog, messagebox
from ocr_logic import ocr_image, save_as_txt, save_as_pdf

def start_gui():
    root = tk.Tk()
    root.title('Image to Text Converter')
    root.geometry('900x800')

    # extracted text
    text_box = tk.Text(root, height=30, width=90)
    text_box.pack(pady=10)

    # select image button
    def select_image():
        file_paths = filedialog.askopenfilenames(
            filetypes=[('Image Files', '*.png *.jpg *.jpeg *.bmp')],
            title='Select image(s)'
        )

        for path in file_paths:
            text = ocr_image(path)
            text_box.insert(tk.END, text + "\n\n")
            
    def save_txt():
        text = text_box.get('1.0', tk.END).strip() # extract text from text box, from 1st char (1.0) to end
        if not text:
            messagebox.showwarning('No text found!', 'Upload an image.')
            return
        save_as_txt(text)

    def save_pdf():
        text = text_box.get('1.0', tk.END).strip()
        if not text:
            messagebox.showwarning('No text found!', 'Upload an image.')
            return
        save_as_pdf(text)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    tk.Button(button_frame, text='Select image(s)', command=select_image).pack(side='left', padx=5)
    tk.Button(button_frame, text='Save as .txt', command=save_txt).pack(side='left', padx=5)
    tk.Button(button_frame, text='Save as .pdf', command=save_pdf).pack(side='left', padx=5)

    root.mainloop()
