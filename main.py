#Autore: Sossio Giallaurito
#Probelma: hack@napoli 2021
#   La tua astronave è dotata di un certo numero di contenitori ognuno dei quali
#   ha una sua capienza in litri. Il tuo compito è raccogliere liquidi presenti
#   sui pianeti e riempire il più possibile i tuoi contenitori, ma devi fare
#   attenzione a non mescolare diversi liquidi nello stesso contenitore e a
#   non sprecare il carburante a tua disposizione.
#   Ogni spostamento da un pianeta ad un altro richiede una certa quantità di
#   carburante ed ogni pianeta è caratterizzato da una certa quantità di liquidi
#   presenti su di esso. Il tuo obiettivo è cercare di riempire al massimo i contenitori
#   della tua astronave cercando di visitare il maggior numero di pianeti con il
#   carburante a tua disposizione

#Importazione dei modelli dei dati
from models.pianeta import Pianeta
from models.ambiente import Ambiente
from models.stato import Stato

#Moduli procedurali
import functions as f

#Definizioni costanti
nomefile = "data/input" #nome file contenenti i dati con la struttura definita sopra

#Definizioni variabili d'ambiente
pianeta_iniziale = 0 
ambiente = Ambiente() #descrizione dell'ambiente
stato = None

############### Main ##############

def main():

    f.inizializza_dati(nomefile, ambiente)
    stato = Stato(ambiente, pianeta_iniziale)

    print (ambiente)
    print (stato)
    
    f.greedy_distanza_pianeta(ambiente, stato, pianeta_iniziale)
    #stato.stampaCammino(ambiente)

        

    return 0



main()