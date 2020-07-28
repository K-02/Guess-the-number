from random import random

numeroRandom=int(random()*20)
adivino=False
print(numeroRandom) 
while not adivino:
 numero=int(input("Escribe un número"))
 if numero==numeroRandom:
   adivino=True
 elif numero<numeroRandom:
   print("es menor crack")
   
 elif numero>numeroRandom:
   print("es mayor crack")
   
print("Adivinaste!!\PD: Orlando es puto")  
   
