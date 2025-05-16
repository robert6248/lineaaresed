import json
import os

faili_nimi = "kontaktid.json"

def loe_kontaktid_failist():
    if not os.path.exists(faili_nimi):
        return []
    with open(faili_nimi, "r", encoding="utf-8") as f:
        return json.load(f)

def salvesta_kontaktid_faili(kontaktid):
    with open(faili_nimi, "w", encoding="utf-8") as f:
        json.dump(kontaktid, f, ensure_ascii=False, indent=4)

def lisa_kontakt(kontaktid, nimi, telefon, email):
    kontaktid.append({"nimi": nimi, "telefon": telefon, "email": email})

def otsi_kontakt(kontaktid, nimi):
    return [k for k in kontaktid if nimi.lower() in k["nimi"].lower()]

def kustuta_kontakt(kontaktid, nimi):
    leitud = [k for k in kontaktid if k["nimi"].lower() == nimi.lower()]
    if leitud:
        kontaktid.remove(leitud[0])
        return True
    return False

def sorteeri_kontaktid(kontaktid, vaike):
    return sorted(kontaktid, key=lambda x: x[vaike].lower())

def muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, uus_email):
    for k in kontaktid:
        if k["nimi"].lower() == vana_nimi.lower():
            k["nimi"] = uus_nimi
            k["telefon"] = uus_telefon
            k["email"] = uus_email
            return True
    return False

# Новые функции:

def otsi_kontakt_telefoniga(kontaktid, telefon):
    """Поиск контакта по номеру телефона."""
    return [k for k in kontaktid if telefon in k["telefon"]]

def kontaktide_arv(kontaktid):
    """Возвращает количество контактов."""
    return len(kontaktid)

def kustuta_kõik_kontaktid(kontaktid):
    """Удаляет все контакты и сохраняет пустой файл."""
    kontaktid.clear()
    salvesta_kontaktid_faili(kontaktid)

def otsi_kontaktid_emaili_domeeniga(kontaktid, domeen):
    """Поиск контактов по домену электронной почты."""
    return [k for k in kontaktid if domeen in k["email"]]

def kuva_kontaktid_alfabeedi_jargi(kontaktid):
    """Отображение всех контактов в алфавитном порядке по имени."""
    return sorted(kontaktid, key=lambda x: x["nimi"].lower())
