#Autore: Sossio Giallaurito
#Probelma: hack@napoli 2021

from models.pianeta import Pianeta
from models.ambiente import Ambiente
from models.stato import Stato
import os

################# Funzioni gestione file ##################

#Formato file 
#   Riga zero:
#       n_pianeti l_carburante n_contenitori/n_liquidi
#   Riga uno:
#       capacita_contenitore_1 ... capacita_contenitore_n
#   Da riga due a riga n_pianeti + 2
#       id_pianeta litri_liquido_1 .. litri_liquido_n

#   Da riga n_pianeti + 2 fino a eof
#       id_pianeta id_pianeta litri_carburante_trasferimento


def inizializza_dati(nomefile, ambiente : Ambiente):

    f = open(nomefile, "r")

    #Lettura prima riga
    row = f.readline().split(" ")
    n_pianeti = int(row[0])
    ambiente.l_carburante_iniziale = row[1]
    n_contenitori = int(row[2])

    #Lettura seconda riga
    row = f.readline().split(" ")
    if(len(row) == n_contenitori):
        ambiente.dim_contenitori = row
    else:
        print("File compromesso. Numero contenitori dichiarati ("+str(n_contenitori)+") diversi dal numero di specifiche sulla dimesnione dei contenitori ("+str(len(row))+").\n")
        f.close
        return 1

    #Lettura geografia pianeta
    i = 0
    for row in f:
        if i < n_pianeti:
            info_pianeta = row.split(" ")
            if(len(info_pianeta) == n_contenitori + 1):
                nuovo_pianeta = Pianeta()
                nuovo_pianeta.id = int(info_pianeta[0])
                del info_pianeta[0]
                nuovo_pianeta.qta_liquidi = info_pianeta
                ambiente.lista_pianeti.append(nuovo_pianeta)
                i = i+1
                #screen_clear()
                #print("Caricamento geografia pianeta con id:"+str(nuovo_pianeta.id)+"\n")
            else:
                print("File compromesso. La lista dei pianeti con le quantità di liquidi è corrotto.\n")
                break
        else:
            break
    
    #Lettura interdistanza pianeti
    i = 0
    for row in f:
        info_pianeta = row.split(" ")
        id_pianeta_a = int(info_pianeta[0])
        id_pianeta_b = int(info_pianeta[1])
        distanza = int(info_pianeta[2])
        #screen_clear()
        #print("Calcolo coerenza interdistanza tra i pianeti:"+str(id_pianeta_a)+" e "+str(id_pianeta_b)+"\n")
        #if(ambiente.trovaPianeta(id_pianeta_a) >= 0 and ambiente.trovaPianeta(id_pianeta_b) >= 0):
        ambiente.lista_pianeti[id_pianeta_a].lista_pianeti_raggiungibili.append(id_pianeta_b)
        ambiente.lista_pianeti[id_pianeta_a].costo_raggiungimento_pianeta.append(distanza)
        ambiente.lista_pianeti[id_pianeta_b].lista_pianeti_raggiungibili.append(id_pianeta_a)
        ambiente.lista_pianeti[id_pianeta_b].costo_raggiungimento_pianeta.append(distanza)
        #else:
        #    print("File compromesso. La lista della distanza tra i pianeti fa riferimento ad un pianeta che non è presente nella lista ("+info_pianeta[0]+" "+info_pianeta[1]+").\n")
        #    break


    f.close
    print(ambiente)
    print("Ambiente caricato correttamente.\n")

    return 0

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text

def greedy_distanza_pianeta(ambiente : Ambiente, stato: Stato, pianeta_partenza):
    verifica_partenza = ambiente.trovaPianeta(pianeta_partenza)

    if(verifica_partenza >= 0):

        pianeta_corrente = ambiente.lista_pianeti[pianeta_partenza]

        while(not stato.verificaContenitoriVuoti() and stato.l_carburante_attuale >= 0):
            
            costo_pianeta_vantagg = 100000000000000000000000000000000000
            for i in range(1, len(pianeta_corrente.lista_pianeti_raggiungibili)):

                if(not(stato.verificaVisitato(pianeta_corrente.lista_pianeti_raggiungibili[i])) and costo_pianeta_vantagg > pianeta_corrente.costo_raggiungimento_pianeta[i]):
                    pos_pianeta_vantagg = i
                    costo_pianeta_vantagg = pianeta_corrente.costo_raggiungimento_pianeta[i]
                    

            if(pos_pianeta_vantagg < len(pianeta_corrente.lista_pianeti_raggiungibili)):
                pos_pianeta_succ = ambiente.trovaPianeta(pianeta_corrente.lista_pianeti_raggiungibili[pos_pianeta_vantagg])
                pianeta_succ = ambiente.lista_pianeti[pos_pianeta_succ]
                stato.nuovo_viaggio(pianeta_corrente, pianeta_succ)

                pianeta_corrente = pianeta_succ
                pianeta_succ = None
            else:
                print("Non è più possibile spostarsi dal pianeta:\n"+str(pianeta_corrente))
                break

            screen_clear()
            print(stato)