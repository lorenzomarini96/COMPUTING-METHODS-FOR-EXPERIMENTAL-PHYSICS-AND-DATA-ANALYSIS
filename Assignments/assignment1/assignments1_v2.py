import matplotlib.pyplot as plt
import numpy as np
import operator  


def relative_frequence_letter(text):
    
    '''
    Python program that prints the relative frequence of each letter
    of the alphabet (without distinguishing between lower and upper case) in the
    book.
    
    '''
    # Delete unwanted characters.
    text_del = text.maketrans({char: None for char in ""'!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'""})

    # Divide the text word by word.
    text_div = text.lower().translate(text_del).split()  # .lower() returns the string with all letters in lowercase (UPPERCASE -> lowercase)

    # Join the elements of the text list with no space between them.
    text_join = ''.join(text_div)

    def split_char(word): 
        '''
        Function to separate each letter in each word. 
        Maybe not too pythonic...
        '''
        return [char for char in word]

    # New text to be analyzed.
    text_new = split_char(text_join)
    #print(text_new)
    
    
    #------------------------------------------------------------------------

    # Create dictionary
    dict_frequence_letter = {}
    
    for letter in text_new:                            
        if letter in dict_frequence_letter:          
            dict_frequence_letter[letter] += 1       
        else:
            dict_frequence_letter[letter] = 1        
       
    print("\nFrequency dictionary letters of the alphabet:\n", dict_frequence_letter)
   
    list_keys_dict   = list(dict_frequence_letter.keys())
    list_values_dict = list(dict_frequence_letter.values())
    list_items_dict  = list(dict_frequence_letter.items())
   
    print('\n=============================================')
    print(f'\nTotal number of letters in the text: {sum(list_values_dict)}')
    print(f'\nTotal number of letters used: {len(list_keys_dict)}')
    print('\n=============================================\n')
  
    dict_frequence_letter_ordered = dict(sorted(dict_frequence_letter.items(), key=operator.itemgetter(1),reverse=True))
    print(dict_frequence_letter_ordered)

    #------------------------------------------------------------------------

    #=======================
    # Create Histogram
    #=======================

    plt.figure(figsize=(10,6))
    plt.bar(range(len(list_items_dict)), [val[1] for val in list_items_dict], facecolor = 'g',ec = 'black', label="Frequenze", width=0.5)
    #plt.errorbar(range(len(list_items_dict)), [val[1] for val in list_items_dict], np.sqrt([val[1] for val in list_items_dict]), fmt='.', color='black', ecolor='black')
   
    # Bellurie
    plt.suptitle('Histogram frequence letters')
    plt.title('"Inferno - 1° Canto"')
    plt.xlabel('Letters')
    plt.xticks(range(len(list_items_dict)), [val[0] for val in list_items_dict])
    plt.minorticks_on()
    #plt.xticks(rotation=45)
    plt.ylabel('Frequence')
    #plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot diverse = %.i' %len(lista_chiavi_dizionario))
    #plt.plot([], [], color='white', marker='.',linestyle='None', label='# tot parole  = %.i' %sum(lista_valori_dizionario))
    #plt.legend()

    plt.savefig('histogram_freq_letters.pdf', bbox_inches='tight')
    plt.show()

# test
text_test = open('inferno.txt', 'r')
text_test = text_test.read().replace("\n", " ") # Togliere gli \n per andare a capo.

relative_frequence_letter(text_test)



