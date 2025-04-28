from funktsioonid import (
    lae_kontaktid, salvesta_kontaktid, lisa_kontakt,
    kuva_kontaktid, otsi_kontakt, kustuta_kontakt,
    muuda_kontakt, sorteeri_kontaktid, saada_email
)

def peamenüü():
    kontaktid = lae_kontaktid()

    while True:
        print("\nTelefoniraamat:")
        print("1. Lisa kontakt")
        print("2. Kuva kõik kontaktid")
        print("3. Otsi kontakti nime järgi")
        print("4. Kustuta kontakt")
        print("5. Muuda kontakti")
        print("6. Sorteeri kontaktid")
        print("7. Saada e-kiri kontaktile")
        print("8. Välju")

        valik = input("Vali tegevus (1-8): ")

        if valik == "1":
            lisa_kontakt(kontaktid)
        elif valik == "2":
            kuva_kontaktid(kontaktid)
        elif valik == "3":
            otsi_kontakt(kontaktid)
        elif valik == "4":
            kustuta_kontakt(kontaktid)
        elif valik == "5":
            muuda_kontakt(kontaktid)
        elif valik == "6":
            sorteeri_kontaktid(kontaktid)
        elif valik == "7":
            saada_email(kontaktid)
        elif valik == "8":
            salvesta_kontaktid(kontaktid)
            print("Head aega!")
            break
        else:
            print("Vale valik. Proovi uuesti.")

        salvesta_kontaktid(kontaktid)

peamenüü()
