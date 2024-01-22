'''
Define a function to count the frequency of words in a given list of words, then index them in a dictionary. 
Example:
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output:
 {'apple': 3, 'orange': 2, 'banana': 1}
'''


def wordFrecuency(words):  
  
    my_dict = {}.fromkeys(words, 0)
    for element in my_dict:
        valor = words.count(element)
        my_dict[element] = valor
    
    return print(my_dict)


words = ['apple', 'orange', 'eggs', 'banana', 'apple', 'orange', 'apple', 'bread', 'banana', 'eggs']
wordFrecuency(words)

