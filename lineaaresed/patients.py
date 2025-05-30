import random

def create_patients(n):
    nimed = []
    vitamiinid = []
    for i in range(n):
        nimi = input(f"Sisesta patienti nimi {i+1}: ")
        vit = random.randint(10, 100)  
        nimed.append(nimi)
        vitamiinid.append(vit)
    return nimed, vitamiinid

def patients_below_30(n, nimed, vitamiinid):
    result = []
    for i in range(n):
        if vitamiinid[i] < 30:
            result.append((nimed[i], vitamiinid[i]))
    return result

def average_vitamin_level(vitamiinid):
    return sum(vitamiinid) / len(vitamiinid)

def top_k_patients(k, nimed, vitamiinid):
    patients = list(zip(nimed, vitamiinid))
    sorted_patients = sorted(patients, key=lambda x: x[1], reverse=True)
    return sorted_patients[:k]

def search_patient(name, nimed, vitamiinid):
    result = []
    for i in range(len(nimed)):
        if name.lower() in nimed[i].lower():
            result.append((nimed[i], vitamiinid[i]))
    return result
