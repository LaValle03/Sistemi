class Nodo:
    def __init__(self,valore):
        self.sinistra = None
        self.destra = None
        self.valore = valore
    
    def inserisci(self,valore):
        if self.valore != None :
            if valore < self.valore :
                if self.sinistra is None :
                    self.sinistra = Nodo(valore)
                else :
                    self.sinistra.inserisci(valore)
            elif valore > self.valore :
                if self.destra is None :
                    self.destra = Nodo(valore)
                else:
                    self.destra.inserisci(valore)
            else:
                self.valore = valore
        else:
            self.valore = valore 
    
    def stampaAlbero(self):
        if self.sinistra:
            self.sinistra.stampaAlbero()
        
        print(self.valore)

        if self.destra:
            self.destra.stampaAlbero()
    
    def attraversamento_ordine(self, albero):
        res = []

        if albero:
            res = self.attraversamento_ordine(albero.sinistra)
            res.append(albero.valore)
            res = res + self.attraversamento_ordine(albero.destra)
        
        return res

    def attraversamento_preordine(self, albero):
        res = []

        if albero:
            res.append(albero.valore)
            res = res + self.attraversamento_preordine(albero.sinistra)
            res = res + self.attraversamento_preordine(albero.destra)
        
        return res

    def attraversamento_postordine(self, albero):
        res = []

        if albero:
            res = self.attraversamento_postordine(albero.sinistra)
            res = res + self.attraversamento_postordine(albero.destra)
            res.append(albero.valore)
        
        return res

    def somma(self):
        somma = 0
        lista = self.attraversamento_ordine(self)

        for numero in lista: 
            somma = somma + numero

        return somma

    def pari(self):
        lista = self.attraversamento_ordine(self)
        listaPari = []

        for k in range(len(lista)):
            if lista[k] % 2 == 0:
                listaPari.append(lista[k])

        return listaPari

albero = Nodo(27)

albero.inserisci(27)
albero.inserisci(14)
albero.inserisci(10)
albero.inserisci(19)
albero.inserisci(35)
albero.inserisci(31)
albero.inserisci(42)

print(albero.somma())
print(albero.pari())