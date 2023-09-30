import tkinter as tk
from download import download 

def button_click():
    input_text = textbox.get("1.0", "end-1c")  # Metin kutusundan girilen değeri al
    print("Girilen metin:", input_text)
    download(input_text)

# Pencere oluşturma
window = tk.Tk()
window.title("Frame Örneği")
window.geometry("250x300")
window.configure(bg="cyan")

# Metin kutusu oluşturma
textbox = tk.Text(window, height=5, width=30)
textbox.pack(pady=10)

# Düğme oluşturma
button = tk.Button(window, text="Download", command=button_click)
button.pack()

# Pencereyi çalıştırma
window.mainloop()
