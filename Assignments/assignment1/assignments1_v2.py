import matplotlib.pyplot as plt
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
        '''
        return [char for char in word]

    # New text to be analyzed.
    text_new = split_char(text_join)
    print(text_new)
    
    
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
    list_itmes_dict  = list(dict_frequence_letter.items())
   
   
    #input(" ")
    print('\n=============================================')
    print('\nTotal number of letters in the text: %.i'  %(sum(list_values_dict)))
    print('\nTotal number of letters used: %.i' %(len(list_keys_dict)))
    print('\n=============================================\n')
    #input(" ")


    dict_frequence_letter_ordered = dict(sorted(dict_frequence_letter.items(), key=operator.itemgetter(1),reverse=True))
    print(dict_frequence_letter_ordered)
    
    
# test
testo = 'Ciao a tutti quanti!.'

relative_frequence_letter(testo)