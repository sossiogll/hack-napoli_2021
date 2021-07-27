#Autore: Sossio Giallaurito
#Probelma: hack@napoli 2021

#L'identificazione dei contenitori e dei liquidi è relativa alla loro posizine nel vettore.
#Questo significa che la dimensione dei vettori della quantità dei liquidi in un pianeta, e della quantità dei liquidi
#di un contenitore è uguale


class Ambiente:

    def __init__(self, lista_pianeti = None, l_carburante_iniziale = 0, dim_contenitori = None):

        self._l_carburante_iniziale = l_carburante_iniziale

        if(lista_pianeti == None):
            self._lista_pianeti = []
        else:
            self._lista_pianeti = lista_pianeti

        if(dim_contenitori == None):
            self._dim_contenitori = []
        else:
            self._dim_contenitori = dim_contenitori

    def __repr__(self):
        classRepresentation = ""
        classRepresentation += "Numero pianeti trovati: " + str(len(self._lista_pianeti)) + "\n"
        classRepresentation += "Carburante iniziale: " + str(self._l_carburante_iniziale) + "\n"

        if self._dim_contenitori != None:
            classRepresentation += "Numero contenitori e liquidi: " + str(len(self._dim_contenitori)) + "\n"
            classRepresentation += "Capienza massima contenitori a bordo:\n"
            for i in range(0, len(self._dim_contenitori)):
                classRepresentation += "    Contenitore [" + str(i) + "]: " + str(self._dim_contenitori[i]) + "\n"
        else:
            classRepresentation += "Numero contenitori a bordo: 0.\n"

        return classRepresentation

    #Getter

    @property
    def lista_pianeti(self):
        return self._lista_pianeti

    @property
    def l_carburante_iniziale(self):
        return self._l_carburante_iniziale

    @property
    def dim_contenitori(self):
        return self._dim_contenitori

    #Setter

    @lista_pianeti.setter
    def lista_pianeti(self, value):
        self._lista_pianeti = value

    @l_carburante_iniziale.setter
    def l_carburante_iniziale(self, value):
        self._l_carburante_iniziale = int(value)

    @dim_contenitori.setter
    def dim_contenitori(self, value):
        self._dim_contenitori = value

    
    def trovaPianeta(self, id):

        risultato = -1

        for i in range(0, len(self.lista_pianeti)):
            if(int(id) == int(self.lista_pianeti[i].id)):
                risultato = i
                break
        
        return risultato


