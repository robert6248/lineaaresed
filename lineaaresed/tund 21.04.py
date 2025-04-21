andmed={}
andmed = {'nimi': 'Mari', 'vanus': 25, 'keel': 'eesti'}
andmed = dict(nimi='Mari', vanus=25, keel='eesti')
print(andmed)
print(andmed['nimi'])
print(andmed.get('nimi'))
print(andmed.get('nimi_', "Ei ole sõnastikus"))
print(andmed.keys())
print(andmed.values())
for k, v in andmed.items():
    print(k, v)
andmed['email'] = 'abcd.efg@gmail.com'
print(andmed)
andmed['prillid']=True
print(andmed)
del andmed['prillid']
print(andmed)
andmed.update({'nimi':'Kati'})
read=['Mis on Python?-programmeerimiskeel', 'Eesti pealinn?-Tallinn']
kus_vas = {}
for rida in read:
    kysimus, vastus = rida.split('-')
    kus_vas[kysimus.strip()] = vastus.strip()
print(kus_vas)

kysimused = list(kus_vas.keys())
n=randint(0, len(read)-1)
valitud_kysimus = kysimused[n]
print(valitud_kysimus)
vastus=input("Sisesta vastus: ")
if vastus == kus_vas[valitud_kysimus]:
    print("Õige vastus!")  
else:
    print("Vale vastus!")