# az alkalamazás itt fut

from dolgozok import Dolgozok


class Ber:
    #konstruktor, az osztály változoknak kezdo értéket adunk
    def __intit__(self):
        self.filename = "berkft.txt"
        self.dolgozokLista = []
        
    # fájl beolvasása:
    def olvas_fajl(self):
        fp = open(self.filename, "r", encoding="utf-8")    
        lines = fp.readlines()
        fp.close()
        for line in lines :
            line = line.rstrip()
            (nev, telepules, cim, szuletes, fizetes) = line.split(":")
            dolgozok = Dolgozok(nev, telepules, cim, szuletes, fizetes)
            self.dolgozokLista.append(dolgozok)
            print(dolgozok.nev)
        
    #szlnokiak 
    def szolnoki(self):
        szolnokiLista = []
        for dolgozok in self.dolgozokLista:
            if dolgozok.telepules == "Szolnok":
                szolnokiLista.append(dolgozok)
        #for vege
        #legfiatalabb; minimum kiválasztás tétel 
        
        max_szolnok = szolnokiLista[0]
        for szolnok in szolnokiLista:
            if szolnok.szuletes > max_szolnoki:
        
                max_szolnoki = szolnok


#class ber vege

ber = Ber()        
ber.olvas_fajl()
