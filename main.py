import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
from pdf2docx import Converter
import os

# تحديد مسار Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# وظيفة لتحويل الصورة إلى نص
def convert_image_to_text():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg;*.bmp;*.tiff")])
    if file_path:
        try:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            text_output.delete(1.0, tk.END)
            text_output.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert image: {e}")

# وظيفة لتحويل PDF إلى Word
def convert_pdf_to_word():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        try:
            output_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
            if output_path:
                cv = Converter(file_path)
                cv.convert(output_path, start=0, end=None)
                cv.close()
                messagebox.showinfo("Success", "PDF converted to Word successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert PDF: {e}")

# وظيفة لحفظ النص كملف Word
def save_text_as_word():
    text = text_output.get(1.0, tk.END)
    if text.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(text)
                messagebox.showinfo("Success", "Text saved as Word file successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")
    else:
        messagebox.showwarning("Warning", "No text to save!")

# إنشاء واجهة المستخدم
root = tk.Tk()
root.title("Image and PDF to Text Converter")

# زر لتحويل الصورة إلى نص
btn_image_to_text = tk.Button(root, text="Convert Image to Text", command=convert_image_to_text)
btn_image_to_text.pack(pady=10)

# زر لتحويل PDF إلى Word
btn_pdf_to_word = tk.Button(root, text="Convert PDF to Word", command=convert_pdf_to_word)
btn_pdf_to_word.pack(pady=10)

# زر لحفظ النص كملف Word
btn_save_word = tk.Button(root, text="Save Text as Word", command=save_text_as_word)
btn_save_word.pack(pady=10)

# مربع نص لعرض النص المستخرج
text_output = tk.Text(root, height=20, width=80)
text_output.pack(pady=10)

# تشغيل الواجهة
root.mainloop()
