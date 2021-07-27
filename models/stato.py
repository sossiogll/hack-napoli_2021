#Autore: Sossio Giallaurito
#Probelma: hack@napoli 2021

from models.pianeta import Pianeta
from models.ambiente import Ambiente

class Stato:

    def __init__(self, ambiente : Ambiente, pianeta_partenza):
        self._l_carburante_attuale = ambiente.l_carburante_iniziale
        self._capienza_rimanente_contenitori = ambiente.dim_contenitori
        self._pianeti_visitati = []

        if(ambiente.trovaPianeta(pianeta_partenza) >= 0):
            self._pianeti_visitati.append(ambiente.lista_pianeti[pianeta_partenza])
        

    def __repr__(self):
        classRepresentation = ""
        classRepresentation += "Carburante attuale: " + str(self._l_carburante_attuale) + "\n"

        if self.capienza_rimanente_contenitori != None:
            classRepresentation += "Numero contenitori e liquidi: " + str(len(self.capienza_rimanente_contenitori)) + "\n"
            classRepresentation += "Capienza corrente dei contenitori a bordo:\n"
            for i in range(0, len(self.capienza_rimanente_contenitori)):
                classRepresentation += "    Contenitore [" + str(i) + "]: " + str(self.capienza_rimanente_contenitori[i]) + "\n"
        else:
            classRepresentation += "Numero contenitori a bordo: 0.\n"
        classRepresentation += "Pianeti visitati: "+str(len(self.pianeti_visitati))
        
        return classRepresentation + "\n\n"

    #Getter

    @property
    def l_carburante_attuale(self):
        return self._l_carburante_attuale

    @property
    def capienza_rimanente_contenitori(self):
        return self._capienza_rimanente_contenitori

    @property 
    def pianeti_visitati(self):
        return self._pianeti_visitati

    #Setter

    @l_carburante_attuale.setter
    def l_carburante_attuale(self, value):
        self._l_carburante_attuale= value


    @capienza_rimanente_contenitori.setter
    def capienza_rimanente_contenitori(self, value):
        self._capienza_rimanente_contenitori = value

    @pianeti_visitati.setter
    def pianeti_visitati(self, value):
        self._pianeti_visitati = value

    def nuovo_viaggio(self, pianeta_partenza, pianeta_arrivo):
        ragg_a_b = pianeta_partenza.trovaPianetaDestinazione(pianeta_arrivo)
        radd_b_a = pianeta_arrivo.trovaPianetaDestinazione(pianeta_partenza)
        if(ragg_a_b >= 0 and radd_b_a >= 0):
            self.pianeti_visitati.append(pianeta_arrivo)
            self.l_carburante_attuale = int(self.l_carburante_attuale) - int(pianeta_partenza.costo_raggiungimento_pianeta[ragg_a_b])
                
            for i in range(0, len(self.capienza_rimanente_contenitori)):
                self.capienza_rimanente_contenitori[i] = int(self.capienza_rimanente_contenitori[i]) - int(pianeta_arrivo.qta_liquidi[i])
                

    def verificaVisitato(self, id_pianeta):
        for i in range (0, len(self.pianeti_visitati)):
            if(int(self.pianeti_visitati[i].id) == int(id_pianeta)):
                return True
        
        return False

    def verificaContenitoriVuoti(self):
        sono_vuoti = True
        for i in range (0, len(self.capienza_rimanente_contenitori)):
            if(int(self.capienza_rimanente_contenitori[i]) >= 0):
                sono_vuoti = False
                break
        
        return sono_vuoti
    
    def stampaCammino(self, ambiente : Ambiente):
        print("########### Stampa cammino effettuato ###########")
        for i in range(0, len(self.pianeti_visitati)):
            print(ambiente.lista_pianeti[self.pianeti_visitati[i].id])
            print(str(self)+"\n")