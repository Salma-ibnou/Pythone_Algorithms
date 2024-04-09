# randint :
# methode 1

import random

numero = random.randint(0, 10)

print(numero)


# methode 1

from random import randint  
numero = randint(0, 10)

print(numero)


# choice :
from random import randint, choice 

char = choice("Hello World")
print(char) 
