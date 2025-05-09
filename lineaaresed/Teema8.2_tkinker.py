from tkinter import *
from tkinter import messagebox

def saada_kiri():
    to = saaja_entry.get()
    subject = teema_entry.get()
    message = kiri_text.get("1.0", END).strip()

    if not to or not message:
        messagebox.showerror("Viga", "Palun täida kõik kohustuslikud väljad.")
    else:
        # Здесь могла бы быть реальная отправка письма
        messagebox.showinfo("Saadetud", f"E-kiri saadeti aadressile: {to}")

# Aken
aken = Tk()
aken.title("E-posti saatja")
aken.geometry("500x400")
aken.configure(bg="#f0f0f0")
aken.resizable(False, False)

# Sildid ja väljad
Label(aken, text="Saaja (To):", bg="#f0f0f0", font=("Arial", 12)).place(x=30, y=30)
saaja_entry = Entry(aken, width=40, font=("Arial", 12))
saaja_entry.place(x=140, y=30)

Label(aken, text="Teema (Subject):", bg="#f0f0f0", font=("Arial", 12)).place(x=30, y=70)
teema_entry = Entry(aken, width=40, font=("Arial", 12))
teema_entry.place(x=140, y=70)

Label(aken, text="Sõnum (Message):", bg="#f0f0f0", font=("Arial", 12)).place(x=30, y=110)
kiri_text = Text(aken, width=50, height=10, font=("Arial", 12))
kiri_text.place(x=30, y=140)

# Nupp
saada_btn = Button(aken, text="Saada", font=("Arial", 13), bg="#4CAF50", fg="white", command=saada_kiri)
saada_btn.place(x=210, y=330)

aken.mainloop()

