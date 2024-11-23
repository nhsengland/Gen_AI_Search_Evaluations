import string
import pandas as pd
import random
import ast

def remove_punctuation(text: str) -> str:
    
    new_string = ""
    
    for char in text:
        if char not in string.punctuation:
            new_string += char

    return new_string

def insert_misspellings(text: str, data: str = "./missp.csv", prob: float = 1) -> str:
    
    misspellings = pd.read_csv(data, index_col=0)
    
    words = text.split(" ")
    new_words = []

    for word in words:
        if (word in misspellings.index) and (random.randint(0,100)/100 <= prob):
            new_word = random.sample(ast.literal_eval(misspellings.loc[word]["misspellings"]),1)[0]
            new_words.append(new_word)
        else:
            new_words.append(word)
        
    return " ".join(new_words)

def insert_typo(text):

    text = list(text)

    number = random.randint(0,5)
    new_charcters = [random.sample(string.digits+string.ascii_letters,1)[0] for i in range(number)]

    for char in new_charcters:
        index = random.randint(0,len(text)-1)
        text[index] = char
    
    return "".join(text)

