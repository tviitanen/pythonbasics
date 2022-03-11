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


import HTTavoiteKirjasto
import numpy


def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("4) Analysoi opiskelijoiden palautusmäärät")
    print("5) Analysoi tuntikohtaiset palautukset")
    print("6) Analysoi aikavälien palautukset")
    print("0) Lopeta")
    valinta = int(input("Valintasi: "))
    return valinta

def paaohjelma():
    jatka = True
    ListaLue = []
    ListaKirjoita = []
    TulosLista = []
    ListaPalautukset = []
    ListaPisteet =[]
    
    while (jatka):

        if (len(ListaLue) > 0):
            print("Anna uusi valinta.")

            
        valinta = valikko()
        
        if (valinta == 1):
            ListaLue = HTTavoiteKirjasto.LueTiedosto(ListaLue)
            
        elif (valinta == 2):
            if (len(ListaLue) == 0):
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
                print("Anna uusi valinta.")
                
            else:
                ListaKirjoita = HTTavoiteKirjasto.Analysoi(ListaLue, ListaKirjoita)
                TulosLista = HTTavoiteKirjasto.Tilasto(ListaKirjoita, TulosLista)
                
        elif (valinta == 3):
            if (len(ListaKirjoita) == 0):
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.\n")
                print("Anna uusi valinta.")
                
            else:
                HTTavoiteKirjasto.Tallenna(ListaKirjoita, TulosLista)

        elif (valinta == 4):
            if (len(ListaLue) == 0):
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
                print("Anna uusi valinta.")
                
            else:
                ListaPalautukset = HTTavoiteKirjasto.OpiskelijaPalautus(ListaLue, ListaPalautukset) # analyysi
                ListaPisteet = HTTavoiteKirjasto.PisteetPalautus(ListaPalautukset, ListaPisteet) # analyysi
                HTTavoiteKirjasto.PalautusTallenna(ListaPisteet) # tietojen tallennus
                
        elif (valinta == 5):
            matriisi = numpy.zeros((15, 25), int) # luodaan sopivan kokoinen matriisi
            
            if (len(ListaLue) == 0):
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
                print("Anna uusi valinta.")
                
            else:
                matriisi = HTTavoiteKirjasto.TuntiPalautus(ListaLue, ListaPalautukset, TulosLista, matriisi) # analyysi
                HTTavoiteKirjasto.TuntiTallenna(matriisi) # tietojen tallennus
            del matriisi
            
        elif (valinta == 6):
            matriisi = numpy.zeros((15, 8), int)
            
            if (len(ListaLue) == 0):
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.\n")
                print("Anna uusi valinta.")
            else:
                matriisi = HTTavoiteKirjasto.AikaAnalyysi(ListaLue, ListaPalautukset, TulosLista, matriisi)
                HTTavoiteKirjasto.AikaTallenna(matriisi)
            del matriisi
            
        elif (valinta == 0):
            jatka = False
            ListaLue.clear()
            ListaKirjoita.clear()
            print("Kiitos ohjelman käytöstä.")
            
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
            print("Anna uusi valinta.")
            
    ListaLue.clear()
    ListaKirjoita.clear()
    TulosLista.clear()
    ListaPalautukset.clear()
    ListaPisteet.clear()
    return None

paaohjelma()
