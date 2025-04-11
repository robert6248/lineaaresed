from module_palgad import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    print("Andmed: ")
    print(inimesed)
    print(palgad)
    print("Vajuta:\n1-Andmete lisamiseks\n2-Andmete kustutamiseks nime järgi\n3-Leida kes saab kätte suurim palk\n4-Leida kes saab kätte kõige väiksem palk ja milline ta on\n5-Järjestada palgad kasvavas järjekorras koos nimedega\n6-Järjestada palgad kahanevas järjekorras koos nimedega\n7-Teada saada, kes saavad võrdset palka, leida, kui palju neid on ja kuvada nende andmed ekraanile\n8-Teha palgaotsing isiku nime järgi\n9-Väljundab nimekirja inimestest (koos palgaga), kes saavad rohkem/vähem kui määratud summa.")
    v=int(input())
    if v==1:
        k=int(input("Kui palju inimesi sa tahad lisa?: "))
        for i in range(k):
            Lisa_andmed(palgad,inimesed)
    elif v==2:
        Kustuta_andmed(palgad,inimesed)
    elif v==3:
        Suurim_palk(palgad,inimesed)
    elif v==4:
        Väiksem_palk(palgad,inimesed)
    elif v==5:
        palgad,inimesed=sorteerimine_kasvav(palgad,inimesed)
        print(palgad,inimesed)
    elif v==6:
        palgad,inimesed=sorteerimine_kahanev(palgad,inimesed)
        print(palgad,inimesed)
    elif v==7:
        Võrdsed_palgad(palgad,inimesed)
    elif v==8:
        palgaotsing(palgad,inimesed)
    elif v==9:
        filtr_palgad(palgad,inimesed)