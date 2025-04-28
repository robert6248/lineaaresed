import json
import os
import smtplib
from email.message import EmailMessage

FAILINIMI = "kontaktid.json"

# Laeb kontaktid failist
def lae_kontaktid():
    if not os.path.exists(FAILINIMI):
        salvesta_kontaktid([])
    with open(FAILINIMI, "r", encoding="utf-8") as f:
        kontaktid = json.load(f)
    return kontaktid

# Salvestab kontaktid faili
def salvesta_kontaktid(kontaktid):
    with open(FAILINIMI, "w", encoding="utf-8") as f:
        json.dump(kontaktid, f, indent=2)

# Lisab uue kontakti
def lisa_kontakt(kontaktid):
    nimi = input("Sisesta nimi: ")
    telefon = input("Sisesta telefon: ")
    email = input("Sisesta e-mail: ")
    kontakt = {"nimi": nimi, "telefon": telefon, "email": email}
    kontaktid.append(kontakt)
    print("Kontakt lisatud!")

# Kuvab kõik kontaktid
def kuva_kontaktid(kontaktid):
    if not kontaktid:
        print("Kontaktide nimekiri on tühi.")
    else:
        for kontakt in kontaktid:
            print(f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}")

# Otsib kontakti nime järgi
def otsi_kontakt(kontaktid):
    otsing = input("Sisesta nimi otsimiseks: ").lower()
    leitud = False
    for kontakt in kontaktid:
        if otsing in kontakt['nimi'].lower():
            print(f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}")
            leitud = True
    if not leitud:
        print("Kontakti ei leitud.")

# Kustutab kontakti nime järgi
def kustuta_kontakt(kontaktid):
    nimi = input("Sisesta kustutatava kontakti nimi: ").lower()
    for kontakt in kontaktid:
        if nimi in kontakt['nimi'].lower():
            kontaktid.remove(kontakt)
            print("Kontakt kustutatud!")
            return
    print("Kontakti ei leitud.")

# Muudab kontakti andmeid
def muuda_kontakt(kontaktid):
    nimi = input("Sisesta muudetava kontakti nimi: ").lower()
    for kontakt in kontaktid:
        if nimi in kontakt['nimi'].lower():
            uus_nimi = input(f"Uus nimi ({kontakt['nimi']}): ")
            uus_telefon = input(f"Uus telefon ({kontakt['telefon']}): ")
            uus_email = input(f"Uus e-mail ({kontakt['email']}): ")
            if uus_nimi:
                kontakt['nimi'] = uus_nimi
            if uus_telefon:
                kontakt['telefon'] = uus_telefon
            if uus_email:
                kontakt['email'] = uus_email
            print("Kontakt muudetud!")
            return
    print("Kontakti ei leitud.")

# Sorteerib kontaktid valitud välja järgi
def sorteeri_kontaktid(kontaktid):
    väli = input("Sorteeri (nimi, telefon või email): ").lower()
    if väli in ["nimi", "telefon", "email"]:
        kontaktid.sort(key=lambda kontakt: kontakt[väli])
        print(f"Kontaktid sorditud {väli} järgi.")
    else:
        print("Vale valik.")

# Saadab e-maili kontaktile
def saada_email(kontaktid):
    nimi = input("Sisesta kontakti nimi, kellele saata e-mail: ").lower()
    for kontakt in kontaktid:
        if nimi in kontakt['nimi'].lower():
            saatja_email = input("Sisesta oma Gmaili aadress: ")
            saatja_parool = input("Sisesta oma Gmaili parool: ")
            sisu = input("Sisesta sõnum: ")
            try:
                msg = EmailMessage()
                msg.set_content(sisu)
                msg["Subject"] = "Sõnum"
                msg["From"] = saatja_email
                msg["To"] = kontakt["email"]

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(saatja_email, saatja_parool)
                    smtp.send_message(msg)
                print("E-mail saadetud!")
            except Exception as e:
                print("Viga e-maili saatmisel:", e)
            return
    print("Kontakti ei leitud.")
