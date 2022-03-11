######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Teemu Viitanen
# Opiskelijanumero: 00456573
# Päivämäärä: 15.11.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# --
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################


import sys
import numpy
import datetime

class TIEDOT:
    aika = ""
    opiskelija = ""
    tehtava = ""
    
class TULOKSET:
    tehtava = ""
    tehtavien_lkm = ""
    
class OPISKELIJA:
    opiskelija = ""
    palautus_lkm = ""
    
class PALAUTUKSET:
    pisteet = ""
    opiskelija_lkm = ""
    
class AIKA:
    viikko = ""
    aikavali = ""
    palautukset = ""
    



def LueTiedosto(lista):
    lista.clear()
    TiedostoLue =input("Anna luettavan tiedoston nimi: ")

    try:
        tiedosto = open(TiedostoLue, "r")
        tiedosto.readline() # otsikkorivin ohitus
        while (True):
            rivi = tiedosto.readline()
            rivi = rivi[:-1]
            if (len(rivi) == 0):
                break
            sarake = rivi.split(';')
            data = TIEDOT()
            data.aika = sarake [0]
            data.opiskelija = sarake [1]
            data.tehtava = sarake[2]
            lista.append(data)
            lkm = len(lista) # palautusten eli rivien/olioiden lukumäärä
        tiedosto.close()
        print("Tiedostosta '" + TiedostoLue + "' luettiin listaan",
              lkm, "datarivin tiedot.\n")
    except Exception:
        print("Tiedoston '" + TiedostoLue + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return lista



def Analysoi(ListaLue, ListaKirjoita):
    ListaKirjoita.clear()
    
    lkm = (len(ListaLue)) # palautusten eli rivien/olioiden lukumäärä
    tehtavien_lkm = 0
    olio = ListaLue[0]
    tehtava = olio.tehtava # vertailu arvo
    
    for data in ListaLue:
        if (tehtava == data.tehtava):
            tehtavien_lkm += 1 # palautettujen eri tehtävien lukumäärä
            
        else:
            tulos = TULOKSET() # luodaan olio tuloksille
            tulos.tehtava = tehtava 
            tulos.lkm = tehtavien_lkm
            tehtavien_lkm = 1
            ListaKirjoita.append(tulos) # lisätään tulos- olio listaan
            tehtava = data.tehtava

    viimeinen = TULOKSET()  # lisätään viimeinen tehtävä listaan
    viimeinen.tehtava = tehtava
    viimeinen.lkm = tehtavien_lkm
    ListaKirjoita.append(viimeinen)

    print("Analysoitu", lkm, "palautusta", len(ListaKirjoita), "eri tehtävään.")
    print("Tilastotiedot analysoitu.\n")
    return ListaKirjoita



def Tilasto(ListaKirjoita, TulosLista):
    TulosLista.clear()
    palautus_lkm = 0

    teht_lkm = len(ListaKirjoita) # palautettujen eri tehtävien lukumäärä
    palautus = ListaKirjoita[0] # poimitaan listalta 1. olio
    
    min_palautus = palautus.lkm # oliosta vertailtava kohde
    max_palautus = palautus.lkm # oliosta vertailtava kohde
    
    for tulos in ListaKirjoita: # vertailu
        palautus_lkm += tulos.lkm
        if (min_palautus >= tulos.lkm):
            min_palautus = tulos.lkm
            min_tehtava = tulos.tehtava
        if (max_palautus <= tulos.lkm):
            max_palautus = tulos.lkm
            max_tehtava = tulos.tehtava

    palautus_ka = int(int(palautus_lkm) / int(teht_lkm)) # keskimääräiset palautukset
    TulosLista.append(palautus_lkm)
    TulosLista.append(teht_lkm)
    TulosLista.append(palautus_ka)
    TulosLista.append(max_palautus)
    TulosLista.append(max_tehtava)
    TulosLista.append(min_palautus)
    TulosLista.append(min_tehtava)
    return TulosLista



def Tallenna(ListaKirjoita, TulosLista):
    TiedostoKirjoita = input("Anna kirjoitettavan tiedoston nimi: ")
    
    try:
        tiedosto = open(TiedostoKirjoita, "w")
    
        print("Palautuksia tuli yhteensä", str(TulosLista[0]) + ",", str(TulosLista[1]), "eri tehtävään.")
        print("Viikkotehtäviin tuli keskimäärin", str(TulosLista[2]), "palautusta.")
        print("Eniten palautuksia,", str(TulosLista[3]) +", tuli viikkotehtävään", str(TulosLista[4]) + ".")
        print("Vähiten palautuksia,", str(TulosLista[5]) + ", tuli viikkotehtävään", str(TulosLista[6]) + ".\n")
        print("Tehtävä;Lukumäärä")
    
        tiedosto.write("Palautuksia tuli yhteensä " + str(TulosLista[0]) + ", " + str(TulosLista[1]) + " eri tehtävään.\n")
        tiedosto.write("Viikkotehtäviin tuli keskimäärin " + str(TulosLista[2]) + " palautusta.\n")
        tiedosto.write("Eniten palautuksia, " + str(TulosLista[3]) +", tuli viikkotehtävään " + str(TulosLista[4]) + ".\n")
        tiedosto.write("Vähiten palautuksia, " + str(TulosLista[5]) + ", tuli viikkotehtävään " + str(TulosLista[6]) + ".\n\n")

        tiedosto.write("Tehtävä;Lukumäärä\n")
        for data in ListaKirjoita:
            print(str(data.tehtava) + ";" + str(data.lkm))
            tiedosto.write(str(data.tehtava) + ";" + str(data.lkm) + "\n")
        
        print("Tulokset tallennettu tiedostoon '" + TiedostoKirjoita + "'.\n")
        tiedosto.close()
        
    except Exception:
        print("Tiedoston '" + TiedostoKirjoita + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    ListaKirjoita.clear()
    TulosLista.clear()
        
    return None



def OpiskelijaPalautus(ListaLue, ListaPalautukset):
    ListaPalautukset.clear()

    palautukset = sorted(ListaLue, key=lambda x: x.opiskelija) # järjestetään lista opiskelijoiden mukaan
    tehtavien_lkm = 0
    olio = palautukset[0]
    opiskelija = olio.opiskelija # vertailu arvo
    
    for data in palautukset:
        if (opiskelija == data.opiskelija):
            tehtavien_lkm += 1 # palautettujen eri tehtävien lukumäärä
        else:
            tulos = OPISKELIJA() # luodaan olio tuloksille
            tulos.opiskelija = opiskelija 
            tulos.palautus_lkm = tehtavien_lkm
            tehtavien_lkm = 1
            
            ListaPalautukset.append(tulos) # lisätään tulos- olio listaan
            opiskelija = data.opiskelija

    viimeinen = OPISKELIJA()  # lisätään viimeinen opiskelija listaan
    viimeinen.opiskelija = opiskelija
    viimeinen.palautus_lkm = tehtavien_lkm
    ListaPalautukset.append(viimeinen) 
    
    return ListaPalautukset # lista jossa opiskelija ja opiskelijan palauttamien tehtävien lukumäärä


    
def PisteetPalautus(ListaPalautukset, ListaPisteet):
    
    pisteet = sorted(ListaPalautukset, key=lambda x: x.palautus_lkm) # järjestetään lista palautettujen tehtävien mukaan
    oppilaiden_lkm = 0
    olio = pisteet[0]
    opiskelijat = olio.palautus_lkm # vertailu arvo
    
    for data in pisteet: # luodaan lista jonka alkiot järjestetty pisteiden mukaan
    
        if (opiskelijat == data.palautus_lkm):
            oppilaiden_lkm += 1 # tietyn pistemäärän saavuttaneiden oppilaiden lukumäärä
            
        else:
            tulos = PALAUTUKSET() # luodaan olio tuloksille
            tulos.pisteet = opiskelijat
            tulos.palautus_lkm = oppilaiden_lkm
            oppilaiden_lkm = 1
            
            ListaPisteet.append(tulos) # lisätään tulos- olio listaan
            opiskelijat = data.palautus_lkm

    viimeinen = PALAUTUKSET()  # lisätään viimeinen piste listaan
    viimeinen.pisteet = opiskelijat
    viimeinen.palautus_lkm = oppilaiden_lkm
    ListaPisteet.append(viimeinen)
    
    ListaPisteet = sorted(ListaPisteet, key=lambda x: x.pisteet) # järjestetään lista pisteiden mukaan

    lista = list(range(61)) # lista 0-60
    
    x = 0
    y = 0
    
    for i in lista:
        olio = ListaPisteet[y]
        tyhja = lista[x]
        
        if (int(tyhja) != int(olio.pisteet)): # luodaan tyhjät alkiot, eli ne pisteet joita kukaan ei saanut
            tyhja = PALAUTUKSET()
            tyhja.pisteet = x
            tyhja.palautus_lkm = 0
            ListaPisteet.append(tyhja)
            x += 1
            
        else:
            x += 1
            y += 1

            
    ListaPisteet = sorted(ListaPisteet, key=lambda x: x.pisteet) # järjestetään uudelleen
    lista.clear()
    ListaPalautukset.clear()
    
    print("Tehtäväkohtaiset pisteet analysoitu.")
    return ListaPisteet
    
def PalautusTallenna(ListaPisteet):
    nimi = input("Anna kirjoitettavan tiedoston nimi: ")
    
    try:
        tiedosto = open(nimi, "w")
        tiedosto.write("Pistemäärä;Opiskelijoita\n")
        
        for data in ListaPisteet:
            tiedosto.write(str(data.pisteet) + ";" + str(data.palautus_lkm) + "\n")
        
    except Exception:
        print("Tiedoston '" + nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    print("Tulokset tallennettu tiedostoon '" + nimi + "'.\n")
    tiedosto.close()
    ListaPisteet.clear()
    
    return None



def TuntiPalautus(ListaLue, ListaPalautukset, TulosLista, matriisi):
    ListaPalautukset.clear()
    TulosLista.clear()
    
    for data in ListaLue:
        viikko = data.tehtava.split("-")
        viikko = viikko[0]
        viikko = viikko[1:]
        aika = datetime.datetime.strptime(data.aika, "%d-%m-%Y %H:%M:%S")
        tunti = datetime.datetime.strftime(aika, "%H")
        olio = AIKA()
        olio.viikko = viikko
        olio.aikavali = tunti
        ListaPalautukset.append(olio)
        
    ekatunti = ListaPalautukset[0]
    ekatunti = ekatunti.aikavali
    palautukset = 0
    ekaviikko = ListaPalautukset[0]
    ekaviikko = ekaviikko.viikko
    
    for data in ListaPalautukset: # yhdistetään saman viikon samana tuntina tulleet palautukset
        if (ekatunti == data.aikavali and ekaviikko == data.viikko):
            palautukset += 1
            
        else:
            tulos = AIKA()
            tulos.viikko = ekaviikko
            tulos.aikavali = ekatunti
            tulos.palautukset = palautukset
            TulosLista.append(tulos)
            palautukset = 1
            ekatunti = data.aikavali
            ekaviikko = data.viikko
            
    viimeinen = AIKA()  # lisätään viimeinen palautus listaan
    viimeinen.viikko = ekaviikko
    viimeinen.aikavali = ekatunti
    viimeinen.palautukset = palautukset
    TulosLista.append(viimeinen)
            
    for alkio in TulosLista:
        viikko = int(alkio.viikko)
        tunti = int(alkio.aikavali)
        matriisi[viikko][tunti] += alkio.palautukset
            
    print("Tuntikohtaiset palautukset analysoitu.")
    TulosLista.clear()
    ListaPalautukset.clear()
    return matriisi



def TuntiTallenna(matriisi):
    nimi = input("Anna kirjoitettavan tiedoston nimi: ")

    try:
        tiedosto = open(nimi, "w")
        
        tiedosto.write("Tunti") # otsikkotiedot
        for tunti in range(24):
            tiedosto.write(";" + str(tunti))
        tiedosto.write("\n")
            
        for viikko in range(14): # matriisi
            tiedosto.write("Vko " + str(viikko+1))
            for tunti in range(24):
                tiedosto.write(";" + str(matriisi[viikko+1][tunti]))
            tiedosto.write("\n")
        
    except Exception:
        print("Tiedoston '" + nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    print("Tulokset tallennettu tiedostoon '" + nimi + "'.\n")
    tiedosto.close()
    return None

def AikaAnalyysi(ListaLue, ListaPalautukset, TulosLista, matriisi):
    ListaPalautukset.clear()
    TulosLista.clear()

    for data in ListaLue:
        viikko = data.tehtava.split("-")
        viikko = viikko[0]
        viikko = viikko[1:]
        
        if (int(viikko) < 7): # todelliset viikot jotka suurempia kuin 7 on eri kun ns luentoviikot
            ekapalautus = (int(viikko) - 1) * datetime.timedelta(days=7) + datetime.datetime.strptime("01-09-2020 06:00:00", "%d-%m-%Y %H:%M:%S") # jokaisen viikon ensimmäinen palautusajankohta
            palautus = datetime.datetime.strptime(data.aika, "%d-%m-%Y %H:%M:%S") # tehtävän palautusaika
            erotus = palautus - ekapalautus # timedelta-olio
            aikavali = erotus.days
            olio = AIKA()
            olio.viikko = viikko
            olio.aikavali = erotus
            ListaPalautukset.append(olio) # lista olioita joissa palautuksen viikko ja aikaväli

        elif (int(viikko) == 7): # viikko 7 pituus 2 viikkoa, aikavälit 48h
            ekapalautus = (int(viikko) - 1) * datetime.timedelta(days=7) + datetime.datetime.strptime("01-09-2020 06:00:00", "%d-%m-%Y %H:%M:%S")
            palautus = datetime.datetime.strptime(data.aika, "%d-%m-%Y %H:%M:%S") # tehtävän palautusaika
            erotus = palautus - ekapalautus # timedelta-olio
            aikavali = erotus.days # puolitetaan viikko 7 jossa "14 päivää"
            olio = AIKA()
            olio.viikko = viikko
            olio.aikavali = erotus/2
            ListaPalautukset.append(olio) # lista olioita joissa palautuksen viikko ja aikaväli

        else:
            ekapalautus = (int(viikko)) * datetime.timedelta(days=7) + datetime.datetime.strptime("01-09-2020 06:00:00", "%d-%m-%Y %H:%M:%S")
            palautus = datetime.datetime.strptime(data.aika, "%d-%m-%Y %H:%M:%S") # tehtävän palautusaika
            erotus = palautus - ekapalautus # timedelta-olio
            aikavali = erotus.days
            olio = AIKA()
            olio.viikko = viikko
            olio.aikavali = erotus
            ListaPalautukset.append(olio) # lista olioita joissa palautuksen viikko ja aikaväli

    ekapalautus = ListaPalautukset[0]
    ekavali = ekapalautus.aikavali
    palautukset = 0
    ekaviikko = ListaPalautukset[0]
    ekaviikko = ekaviikko.viikko
    
    for data in ListaPalautukset: # yhdistetään saman viikon samana aikavälina tulleet palautukset
         
        if (ekavali == data.aikavali and ekaviikko == data.viikko):
            palautukset += 1
            
        else:
            tulos = AIKA()
            tulos.viikko = ekaviikko
            tulos.aikavali = ekavali
            tulos.palautukset = palautukset
            TulosLista.append(tulos)
            palautukset = 1
            ekavali = data.aikavali
            ekaviikko = data.viikko

    viimeinen = AIKA()  # lisätään viimeinen palautus listaan
    viimeinen.viikko = ekaviikko
    viimeinen.aikavali = ekavali
    viimeinen.palautukset = palautukset
    TulosLista.append(viimeinen) # lista olioita joissa viikko, aikaväli ja palautusten määrä

    for alkio in TulosLista: # tallennetaan tiedot matriisiin
        viikko = int(alkio.viikko)
        aikavali = int(alkio.aikavali.days)
        matriisi[viikko][aikavali] += alkio.palautukset
        
    print("Aikavälikohtaiset palautukset analysoitu.")
    ListaPalautukset.clear()
    TulosLista.clear()
    return matriisi

def AikaTallenna(matriisi):
    nimi = input("Anna kirjoitettavan tiedoston nimi: ")

    try:
        tiedosto = open(nimi, "w")
        
        tiedosto.write("Aikaväli") # otsikkotiedot
        tiistai = datetime.datetime.strptime("1.9.2020 06:00", "%d.%m.%Y %H:%M")
        for i in range(7):
            tiedosto.write(";" + str(tiistai.strftime("%a %H:%M")))
            tiistai += datetime.timedelta(days=1)
        tiedosto.write("\n")
            
        for viikko in range(14): # matriisi
            tiedosto.write("Vko " + str(viikko+1))
            for aikavali in range(7):
                tiedosto.write(";" + str(matriisi[viikko+1][aikavali]))
            tiedosto.write("\n")
                
    except Exception:
        print("Tiedoston '" + nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
        
    print("Tulokset tallennettu tiedostoon '" + nimi + "'.\n")
    tiedosto.close()
    return None
