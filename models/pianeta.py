#Autore: Sossio Giallaurito
#Probelma: hack@napoli 2021

#L'identificazione dei contenitori e dei liquidi è relativa alla loro posizine nel vettore.
#Questo significa che la dimensione dei vettori della quantità dei liquidi in un pianeta, e della quantità dei liquidi
#di un contenitore è uguale


class Pianeta:

    def __init__(self, id = 0, qta_liquidi = None, lista_pianeti_raggiungibili = None, costo_raggiungimento_pianeta = None):

        self._id = id

        if qta_liquidi == None:
            self._qta_liquidi = []
        else:
            self._qta_liquidi = qta_liquidi

        if lista_pianeti_raggiungibili == None:
            self._lista_pianeti_raggiungibili = []
        else:
            self._lista_pianeti_raggiungibili = lista_pianeti_raggiungibili

        if costo_raggiungimento_pianeta == None:
            self._costo_raggiungimento_pianeta = []
        else:
            self._costo_raggiungimento_pianeta = costo_raggiungimento_pianeta

    def __repr__(self):
        classRepresentation = ""
        classRepresentation += "Identificativo pianeta: " + str(self._id) + "\n"

        if len(self._qta_liquidi) > 0:
            classRepresentation += "Quantità liquidi presenti:\n"
            for i in range(0, len(self.qta_liquidi)):
                classRepresentation += "    Liquido [" + str(i) + "]: " + str(self.qta_liquidi[i]) + "\n"
        else:
            classRepresentation += "Nessun liquido presente sul pianeta.\n"
        
        if len(self._lista_pianeti_raggiungibili) > 0 and len(self.costo_raggiungimento_pianeta) > 0 and len(self.costo_raggiungimento_pianeta) == len(self._lista_pianeti_raggiungibili):
            classRepresentation += "Sono raggiungibili " + str(len(self._lista_pianeti_raggiungibili)) + " pianeti:\n"
            for i in range(0, len(self.lista_pianeti_raggiungibili)):
                classRepresentation += "    Pianeta [" + str(self.lista_pianeti_raggiungibili[i]) + "] con costo " + str(self.costo_raggiungimento_pianeta[i])
        else:
            classRepresentation += "Nessun pianeta raggiungibile o lista pianeti raggiungibili corrotta.\n"

        return classRepresentation

        #Getter

    @property
    def id(self):
        return self._id

    @property
    def qta_liquidi(self):
        return self._qta_liquidi

    @property
    def lista_pianeti_raggiungibili(self):
        return self._lista_pianeti_raggiungibili

    @property
    def costo_raggiungimento_pianeta(self):
        return self._costo_raggiungimento_pianeta

    #Setter

    @id.setter
    def id(self, value):
        self._id = int(value)

    @qta_liquidi.setter
    def qta_liquidi(self, value):
        self._qta_liquidi = value

    @lista_pianeti_raggiungibili.setter
    def lista_pianeti_raggiungibili(self, value):
        self._lista_pianeti_raggiungibili = value

    @costo_raggiungimento_pianeta.setter
    def costo_raggiungimento_pianeta(self, value):
        self._costo_raggiungimento_pianeta = value

    
    def trovaPianetaDestinazione(self, pianeta_destinazione):
        risultato = -1

        for i in range (0, len(self.lista_pianeti_raggiungibili)):
            if(self.lista_pianeti_raggiungibili[i] == int(pianeta_destinazione.id)):
                risultato = i
                break

        return risultato