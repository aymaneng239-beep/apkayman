import tkinter as tk
from tkinter import font

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("عرض الاسم")
root.geometry("400x200")
root.configure(bg='#f0f0f0')

# إنشاء خط عربي
try:
    arabic_font = font.Font(family="Arial", size=40, weight="bold")
except:
    arabic_font = font.Font(size=40, weight="bold")

# إنشاء تسمية لعرض الاسم
label = tk.Label(
    root, 
    text="أيمن", 
    font=arabic_font,
    bg='#f0f0f0',
    fg='#2c3e50'
)
label.pack(expand=True)

# إضافة تسمية إضافية
sub_label = tk.Label(
    root,
    text="مرحباً بك!",
    font=("Arial", 16),
    bg='#f0f0f0',
    fg='#7f8c8d'
)
sub_label.pack()

# تشغيل التطبيق
root.mainloop()
