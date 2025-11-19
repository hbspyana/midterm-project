import tkinter as tk
from tkinter import filedialog, messagebox
from ocr_logic import ocr_image, write_log, save_as_txt, save_as_pdf

def start_gui():
    root = tk.Tk()
    root.title('Image to Text Converter')
    root.geometry('900x800')

    # extracted text
    text_box = tk.Text(root, height=30, width=90)
    text_box.pack(pady=10)

    # select image button
    def select_image():
        file_path = filedialog.askopenfilename(
            filetypes=[('Image Files', '*.png *.jpg *.jpeg *.bmp')],
            title='Select an Image'
        )

        text = ocr_image(file_path)  # extract text
        text_box.delete('1.0', tk.END)
        text_box.insert(tk.END, text)
        messagebox.showinfo('Success', 'Text extracted!')

    def save_txt():
        text = text_box.get('1.0', tk.END).strip()
        if not text:
            messagebox.showwarning('No text', 'There is no text to save!')
            return
        save_as_txt(text)

    def save_pdf():
        text = text_box.get('1.0', tk.END).strip()
        if not text:
            messagebox.showwarning('No text', 'There is no text to save!')
            return
        save_as_pdf(text)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    tk.Button(button_frame, text='Select Image', command=select_image).pack(side='left', padx=5)
    tk.Button(button_frame, text='Save as TXT', command=save_txt).pack(side='left', padx=5)
    tk.Button(button_frame, text='Save as PDF', command=save_pdf).pack(side='left', padx=5)

    root.mainloop()