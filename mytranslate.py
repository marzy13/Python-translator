#!/usr/bin/python3
'''
This program is about a set of actions that a person will take depending on the weather. It is a translator between English and Spanish
'''
EtoS = {'If' : 'Si', 'sunny' : 'Soleda', 'Tomorrow' : 'Manana', 'I' : 'Yo',
        'will' : 'sera', 'go' : 'vamos', 'to' : 'a', 'the' : 'el', 'beach' : 'playa', 'with' : 'con', 'my' : 'mi',
        'friends':'amigos','snows':'nieves','ski':'esqui','resort':'recurso','family':'familia',
        'rains':'lluvias','stay':'permanecer','indoors':'adentro','and':'y',
        'watch':'reloj','favourite':'favorite','movie':'peliculas','weather':'clima','yesterday':'ayer',
        'for':'para','a':'una','hike':'caminata','on':'en',          
        'small':'pequena','hill':'colina','near':'cerca',
        'house':'casa','then':'tomar','dog':'perro','dogs':'perros','out':'afuera','walk':'caminar',
        'Regardless':'independientermente','of':'de','order':'orden','large':'grande',
        'pepperoni':'pepperoni','pizza':'pizza','tomorrow':'manana','dinner':'cena','it':'eso','is':'es','like':'mi gusta','take':'tomar','regardless':'independientemente','two':'dos','best':'el mejor','pizzas':'pizzas','friend':'amigo','a':'uno','mine':'mio','movies':'películas','dogs':'perros','three':'tres','cat':'gata','cats':'gatas'}


StoE = dict([(value,key) for key, value in EtoS.items()])
dicts = {'English to Spanish' : EtoS, 'Spanish to English' : StoE}

def translateWord(word, dictionary) :
    if word in dictionary.keys() :
        return dictionary[word]
    elif word != '' :
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction) :
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for character in phrase :
        if character in letters :
            word = word + character
        else : 
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary) 
    return translation + "."

sentence = 'Regardless of the weather, I will order pepperoni pizzas tomorrow for dinner.'
translated = translate(sentence, dicts, 'English to Spanish')
print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
sentence = ' Yo sera vamos afuera a el playa con dos de mi elmejor amigos'
translated = translate(sentence, dicts, 'Spanish to English')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')





