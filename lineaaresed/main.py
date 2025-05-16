import tkinter as tk
from tkinter import messagebox
import funktsioonid1 as f

# Kontaktide laadimine mällu
kontaktid = f.loe_kontaktid_failist()

# Оформление для кнопок, полей ввода и текста
font = ("Arial", 12)
button_bg = "#4CAF50"
button_fg = "white"
button_hover_bg = "#45a049"
entry_bg = "#f0f0f0"
entry_fg = "#333333"
text_bg = "#f9f9f9"
text_fg = "#333333"
frame_bg = "#e8e8e8"

def kuva_kontaktid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")

def lisa_kontakt():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if nimi and telefon and email:
        f.lisa_kontakt(kontaktid, nimi, telefon, email)
        f.salvesta_kontaktid_faili(kontaktid)
        messagebox.showinfo("Edu", "Kontakt lisatud.")
        nimi_entry.delete(0, 'end')
        telefon_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        kuva_kontaktid()
    else:
        messagebox.showwarning("Tühjad väljad", "Täida kõik väljad.")

def otsi_kontakti_gui():
    nimi = nimi_entry.get()
    tulemused = f.otsi_kontakt(kontaktid, nimi)
    if tulemused:
        kontakt = tulemused[0]
        otsingu_viide.set(kontakt["nimi"])  # salvestame algse nime võrdlemiseks hiljem

        nimi_entry.delete(0, 'end')
        nimi_entry.insert(0, kontakt["nimi"])
        telefon_entry.delete(0, 'end')
        telefon_entry.insert(0, kontakt["telefon"])
        email_entry.delete(0, 'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0", "end")
        tekstikast.insert("end", f"Leitud: {kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showinfo("Tulemus puudub", "Kontakti ei leitud.")

def kustuta_kontakt_gui():
    nimi = nimi_entry.get()
    if f.kustuta_kontakt(kontaktid, nimi):
        f.salvesta_kontaktid_faili(kontaktid)
        messagebox.showinfo("Kustutatud", f"'{nimi}' kustutati.")
        kuva_kontaktid()
    else:
        messagebox.showwarning("Ei leitud", "Kontakti ei leitud.")

def sorteeri_gui():
    kontaktid_sorted = f.sorteeri_kontaktid(kontaktid, "nimi")
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")

def muuda_kontakt_gui():
    vana_nimi = otsingu_viide.get()  # salvestame, millise nimega kontakt oli algselt
    uus_nimi = nimi_entry.get()
    uus_telefon = telefon_entry.get()
    uus_email = email_entry.get()

    if vana_nimi and uus_nimi and uus_telefon and uus_email:
        õnnestus = f.muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, uus_email)
        if õnnestus:
            f.salvesta_kontaktid_faili(kontaktid)
            messagebox.showinfo("Muudetud", f"'{vana_nimi}' andmed on muudetud.")
            kuva_kontaktid()
        else:
            messagebox.showwarning("Tõrge", "Kontakti ei leitud muudatuseks.")
    else:
        messagebox.showwarning("Puuduvad andmed", "Palun täida kõik väljad.")

# Новые функции

def otsi_kontakti_telefoniga_gui():
    telefon = telefon_entry.get()
    tulemused = f.otsi_kontakt_telefoniga(kontaktid, telefon)
    if tulemused:
        tekstikast.delete("1.0", "end")
        for kontakt in tulemused:
            tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showinfo("Tulemus puudub", "Kontakti ei leitud telefoniga.")

def kuva_kontaktide_arv_gui():
    arv = f.kontaktide_arv(kontaktid)
    messagebox.showinfo("Kontaktide arv", f"Kokku kontakte: {arv}")

def kustuta_kõik_kontaktid_gui():
    f.kustuta_kõik_kontaktid(kontaktid)
    messagebox.showinfo("Kõik kustutatud", "Kõik kontaktid on kustutatud.")
    kuva_kontaktid()

def otsi_kontaktid_emaili_domeeniga_gui():
    domeen = email_entry.get()
    tulemused = f.otsi_kontaktid_emaili_domeeniga(kontaktid, domeen)
    if tulemused:
        tekstikast.delete("1.0", "end")
        for kontakt in tulemused:
            tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showinfo("Tulemus puudub", "Kontakti ei leitud emaili domeeniga.")

def kuva_kontaktid_alfabeedi_jargi_gui():
    kontaktid_sorted = f.kuva_kontaktid_alfabeedi_jargi(kontaktid)
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid_sorted:
        tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")


aken = tk.Tk()
aken.title("Telefoniraamat")
aken.geometry("800x600")
aken.configure(bg=frame_bg)

# Sisestusväljad
otsingu_viide = tk.StringVar()
otsingu_viide.set("")

tk.Label(aken, text="Nimi:", bg=frame_bg, font=font).pack(pady=5)
nimi_entry = tk.Entry(aken, font=font, bg=entry_bg, fg=entry_fg)
nimi_entry.pack(pady=5)

tk.Label(aken, text="Telefon:", bg=frame_bg, font=font).pack(pady=5)
telefon_entry = tk.Entry(aken, font=font, bg=entry_bg, fg=entry_fg)
telefon_entry.pack(pady=5)

tk.Label(aken, text="Email:", bg=frame_bg, font=font).pack(pady=5)
email_entry = tk.Entry(aken, font=font, bg=entry_bg, fg=entry_fg)
email_entry.pack(pady=5)

# Контейнер для кнопок
frame_left = tk.Frame(aken, bg=frame_bg)
frame_left.pack(side="left", padx=20, pady=20)

frame_right = tk.Frame(aken, bg=frame_bg)
frame_right.pack(side="right", padx=20, pady=20)

# Кнопки слева
tk.Button(frame_left, text="Lisa kontakt", bg=button_bg, fg=button_fg, font=font, command=lisa_kontakt, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_left, text="Kuva kontaktid", bg=button_bg, fg=button_fg, font=font, command=kuva_kontaktid, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_left, text="Otsi kontakti", bg=button_bg, fg=button_fg, font=font, command=otsi_kontakti_gui, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_left, text="Kustuta kontakt", bg=button_bg, fg=button_fg, font=font, command=kustuta_kontakt_gui, relief="raised", bd=2).pack(side="top", pady=5)

# Кнопки справа
tk.Button(frame_right, text="Sorteeri (nime järgi)", bg=button_bg, fg=button_fg, font=font, command=sorteeri_gui, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_right, text="Muuda kontakt", bg=button_bg, fg=button_fg, font=font, command=muuda_kontakt_gui, relief="raised", bd=2).pack(side="top", pady=5)

# Новые кнопки справа
tk.Button(frame_right, text="Otsi telefoniga", bg=button_bg, fg=button_fg, font=font, command=otsi_kontakti_telefoniga_gui, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_right, text="Kontaktide arv", bg=button_bg, fg=button_fg, font=font, command=kuva_kontaktide_arv_gui, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_right, text="Kustuta kõik", bg=button_bg, fg=button_fg, font=font, command=kustuta_kõik_kontaktid_gui, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_right, text="Otsi domeeni järgi", bg=button_bg, fg=button_fg, font=font, command=otsi_kontaktid_emaili_domeeniga_gui, relief="raised", bd=2).pack(side="top", pady=5)
tk.Button(frame_right, text="Kuva alfab. järjekorras", bg=button_bg, fg=button_fg, font=font, command=kuva_kontaktid_alfabeedi_jargi_gui, relief="raised", bd=2).pack(side="top", pady=5)

tekstikast = tk.Text(aken, height=10, width=50, font=font, bg=text_bg, fg=text_fg)
tekstikast.pack(pady=20)

aken.mainloop()
