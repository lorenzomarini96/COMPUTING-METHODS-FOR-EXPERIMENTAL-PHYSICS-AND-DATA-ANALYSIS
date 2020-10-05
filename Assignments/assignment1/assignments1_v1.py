def Analisi_Frequenza_Parole(testo):
   print('*****************************************')
   print('*        ANALISI FREQUENZA PAROLE       *')
   print('*****************************************\n')

   #=============================================================
   # 1) CREAZIONE DEL DIZIONARIO
   #=============================================================

       
   # Elimina caratteri non voluti
   translate     = testo.maketrans({char: None for char in ""'!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'""})

   # Dividi il testo parola per parola
   testo_pulito  = testo.lower().translate(translate).split()  # .lower() restituisce la stringa con tutte le lettere in minuscolo (MAIUSCOLO --> minuscolo)
   
   # Creo il dizionario
   dizionario_parole_frequenze = {}
    
   for parola in testo_pulito:                            # Per ogni parola nel testo pulito
       if parola in dizionario_parole_frequenze:          # Se la parola esiste già in dizionario
           dizionario_parole_frequenze[parola] += 1       # allora incrementa il valore delle frequenze
       else:
           dizionario_parole_frequenze[parola] = 1        # altrimenti se non esiste ancora, creala
       
   #print("\nTESTO PULITO: ",testo_pulito)
   #print("\nDIZIONARIO PAROLE - FREQUENZE:   ",dizionario_parole_frequenze)
   
   lista_chiavi_dizionario = list(dizionario_parole_frequenze.keys())
   lista_valori_dizionario = list(dizionario_parole_frequenze.values())
   lista_dizionario        = list(dizionario_parole_frequenze.items())
   
   
   input(" ")
   print('\n=============================================')
   print('\nNumero totale di parole  presenti:    ',sum(lista_valori_dizionario))
   print('\nNumero parole differenti utilizzate:  ',len(lista_chiavi_dizionario))
   print('\n=============================================\n')
   #input(" ")

   
   choice = 'y'
   
   while choice == 'y':

       print('OPERAZIONI CHE POSSO FARE:\n')
       print('1) TOP N (le N parole piu'' utilizzate)')
       print('2) SOGLIA SUL VALORE DELLE FREQUENZE')
       print('3) SOGLIA SULLE PAROLE')


       scelta = int(input('\nScegli operazione da eseguire: '))
   

   
       
       #=================================================================
       # 2) CREAZIONE DEL DIZIONARIO ORDINATO (dal piu' frequente al meno)
       #=================================================================
   

       import operator
       dizionario_ordinato = dict(sorted(dizionario_parole_frequenze.items(), key=operator.itemgetter(1),reverse=True))
   
   
       if scelta == 1:
  
           #=================================================================
           # 3) CREAZIONE DEL DIZIONARIO TOP N (i primi N elementi)
           #=================================================================
   
           print('\n#====================================')
           print('1) TOP N (le N parole piu'' utilizzate)')
           print('#====================================\n')



           # Dizionario dei primi n elementi
           n = int(input('Classifica N parole piu'' utilizzate, N = '))
           dizionario_top_n = dict(list(dizionario_ordinato.items())[:n])

           #print("\nDIZIONARIO TOP " +  str(n) + " PAROLE - FREQUENZE:   ", dizionario_top_n)
   
           #=============================================================
           # 3.1) CREAZIONE DEL DATAFRAME
           #=============================================================
           print('\nDATAFRAME PAROLE - FREQUENZE TOP N :')
           tabella_dizionario_top_n       = pd.DataFrame(dizionario_top_n,index=[0])
           tabella_dizionario_top_n_trasp = tabella_dizionario_top_n.T
           print(tabella_dizionario_top_n_trasp)


           #=============================================================
           # 3.2) CREAZIONE ISTOGRAMMA DIZIONARIO
           #=============================================================
           lista_chiavi_dizionario = list(dizionario_top_n.keys())
           lista_valori_dizionario = list(dizionario_top_n.values())
           lista_dizionario        = list(dizionario_top_n.items())

           plt.figure(figsize=(10,6))
           plt.bar(range(len(lista_dizionario)), [val[1] for val in lista_dizionario], color='cyan', edgecolor='black', label="Frequenze", width=0.5)
   
           # Bellurie
           plt.title('Istogramma Top N - frequenze parole')
           plt.xlabel('Parole')
           plt.xticks(range(len(lista_dizionario)), [val[0] for val in lista_dizionario])
           plt.xticks(rotation=45)
           plt.ylabel('Frequeze')
           plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot diverse = %.i' %len(lista_chiavi_dizionario))
           #plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot parole  = %.i' %sum(lista_valori_dizionario))
           plt.legend()

           plt.savefig('Isto_dizionario_top_n.pdf', bbox_inches='tight')
           plt.show()
   
   
       elif scelta == 2:
       
           #=================================================================
           # 4) CREAZIONE DEL DIZIONARIO SOGLIA AI VALUES
           #=================================================================
           print('\n#====================================')
           print('SOGLIA SUL VALORE DELLE FREQUENZE')
           print('#====================================\n')


           soglia = int(input('Valore soglia frequenza: '))
   
           new_chiavi = []
           new_valori = []
           for chiave in dizionario_ordinato:
               if dizionario_ordinato[chiave] >= soglia:
                   new_chiavi.append(chiave)
                   new_valori.append(dizionario_ordinato[chiave])
       
           dizionario_soglia_values = dict(zip(new_chiavi, new_valori))
           # print("\nDIZIONARIO PAROLE - FREQUENZE SOGLIA FREQUENZE:   ",dizionario_soglia_values)
           #=============================================================
           # 4.1) CREAZIONE DEL DATAFRAME
           #=============================================================
           print('\nDATAFRAME PAROLE - FREQUENZE SOGLIA FREQUENZE:')
           tabella_dizionario_soglia_values       = pd.DataFrame(dizionario_soglia_values,index=[0])
           tabella_dizionario_soglia_values_trasp = tabella_dizionario_soglia_values.T
           print(tabella_dizionario_soglia_values_trasp)
   
           #=============================================================
           # 4.2) CREAZIONE ISTOGRAMMA DIZIONARIO
           #=============================================================
           istogramma_data = []
           for chiave, valore in dizionario_soglia_values.items():
               istogramma_data.append((valore, chiave))


           plt.figure(figsize=(8,6))
           bars = plt.bar(range(len(istogramma_data)), [val[0] for val in istogramma_data], color='cyan', edgecolor='black', label="Frequenze", width=0.5)
   
           # Bellurie
           plt.title('Istogramma frequenze parole - Soglia sui valori')
           plt.xlabel('Parole')
           plt.xticks(range(len(istogramma_data)), [val[1] for val in istogramma_data])
           plt.xticks(rotation=45)
           plt.ylabel('Frequeze')
           #plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot diverse = %.i' %len(lista_chiavi_dizionario))
           #plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot parole  = %.i' %sum(lista_valori_dizionario))
           plt.legend()
           plt.savefig('Isto_dizionario_soglia_values.pdf', bbox_inches='tight')
   
           plt.show()
   
       elif scelta == 3:

       
           #=================================================================
           # 5) CREAZIONE DEL DIZIONARIO SOGLIA AI KEYS
           #=================================================================
           print('\n#====================================')
           print('SOGLIA SULLE PAROLE')
           print('#====================================\n')
       
   
           # Chiedo quante parole voglio ricercare nel dizionario
           numero_parole_ricercate = int(input('Quante parole vuoi cercare? '))

           # Crea la lista contenente le parole da cercare
           lista_parole_find = []

           # Ciclo per riempire la lista con le parole da cercare
           for i in range(numero_parole_ricercate):
               parole_ricercate = str(input('Parole ricercate: '))
               lista_parole_find.append(parole_ricercate.lower())

           print('Le parole che vuoi cercare sono: ', lista_parole_find)


           # Crea due liste che rappresenteranno gli elementi del nuovo dizionario
           lista_nuova_chiavi = []
           lista_nuova_valori = []

           # Ciclo per vedere se una chiave in dizionario_parole e' presente nella lista_parole_find
           for parola in lista_parole_find:
               if  parola in dizionario_ordinato:
                   lista_nuova_chiavi.append(parola)
                   lista_nuova_valori.append(dizionario_ordinato[parola])
               else:
                   lista_nuova_chiavi.append(parola)
                   lista_nuova_valori.append(0)
               
           dizionario_soglia_keys = dict(zip(lista_nuova_chiavi, lista_nuova_valori))
           dizionario_soglia_keys = dict(sorted(dizionario_soglia_keys.items(), key=operator.itemgetter(1),reverse=True))

           #=============================================================
           # 5.1) CREAZIONE DEL DATAFRAME
           #=============================================================
           tabella_dizionario_soglia_keys       = pd.DataFrame(dizionario_soglia_keys,index=[0])
           tabella_dizionario_soglia_keys_trasp = tabella_dizionario_soglia_keys.T
           print(tabella_dizionario_soglia_keys)

           #=============================================================
           # 5.2) CREAZIONE ISTOGRAMMA DIZIONARIO
           #=============================================================
           lista_chiavi_dizionario = list(dizionario_soglia_keys.keys())
           lista_valori_dizionario = list(dizionario_soglia_keys.values())
           lista_dizionario        = list(dizionario_soglia_keys.items())
   
           plt.figure(figsize=(10,6))
           plt.bar(range(len(lista_dizionario)), [val[1] for val in lista_dizionario], color='cyan', edgecolor='black', label="Frequenze", width=0.5)
   
           # Bellurie
           plt.title('Istogramma frequenze parole - Soglia sulle chiavi')
           plt.xlabel('Parole')
           plt.xticks(range(len(lista_dizionario)), [val[0] for val in lista_dizionario])
           plt.xticks(rotation=45)
           plt.ylabel('Frequeze')
           plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot diverse = %.i' %len(lista_chiavi_dizionario))
           plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot parole  = %.i' %sum(lista_valori_dizionario))
           plt.legend()

           plt.savefig('Isto_dizionario_soglia_key.pdf', bbox_inches='tight')
           plt.show()

       choice = str(input('Vuoi andare avanti? (y/n): '))
   print('\nCiao ciao...')
       #return dizionario_parole_frequenze, dizionario_top_n, dizionario_soglia_values , dizionario_soglia_keys



#############################################################################


import matplotlib.pyplot as plt
import pandas as pd


testo = open('inferno.txt', 'r')
testo = testo.read().replace("\n", " ")    # Togliere gli \n per andare a capo.
titolo = 'Divina Commedia - Canto1'


Analisi_Frequenza_Parole(testo)
