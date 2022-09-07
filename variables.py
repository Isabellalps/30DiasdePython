#Día 1 de los 30 dias de programación con Python
from cmath import pi
from operator import length_hint
from sre_constants import SRE_INFO_LITERAL


nombre = 'Isabella' 
apellido = 'Lopez'
pais = 'Colombia'
ciudad = 'Roldanillo'
edad = 25
anho = 2022
estado_civil = 'Soltera'
peso = 71 

print(type(nombre))
print(type(edad))

print(len(nombre))
print(len(apellido))

print(len(nombre)==len(apellido))

num1 = 5
num2 = 4
total = (num1 + num2)
dif = (num1-num2)
mult = (num1*num2)
div = (num1/num2)
res = (num2%num1)
exp = (num1**num2)
exdiv = (num1//num2)
areaCirculo = pi*30**2
diametroCirculo = 2*areaCirculo
circunCirculo = diametroCirculo * pi

radio = int(input('Por favor ingrese el radio del círculo: '))
areaCirculo = pi*radio**2
print(areaCirculo)
print(diametroCirculo)
print(circunCirculo)
