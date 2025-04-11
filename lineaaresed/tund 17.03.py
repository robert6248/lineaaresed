sõne="Programmeerimine"
print(sõne)
list_sõne=list(sõne)
print(list_sõne)
print(f"Viies täht: {list_sõne[5]}")
print(f"Sõnes on {len(sõne)} ")
elemendid=[]
for i in range(5):
    elemendid.append(input("[i+1]. element: "))
print(elemendid)
for e in elemendid:
    print(e)
#extend
list_sõne.extend(elemendid)
print(list_sõne)
print(elemendid)
#insert
elemendid.insert(0,"A")
print(elemendid)
#remove
elemendid.remove("A")
print(elemendid)
#pop
elemendid.pop(0) 
elemendid.pop()
print(elemendid)
#index 
ind=list_sõne.index("r")
print(f"Täht r on {ind}-indeksiga")
#count
k=list_sõne.count("r")
print(f"Täht r kohtume {k} korda sõnas {sõne}")
#sort
list_sõne.sort(reverse=True)
print(list_sõne)
#reverse
list_sõne.reverse()
print(list_sõne)
#copy
list_sõne2=list_sõne.copy()
#clear
list_sõne2.clear()
print(list_sõne2) 