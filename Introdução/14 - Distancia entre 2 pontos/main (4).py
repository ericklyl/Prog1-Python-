#Faça um programa que recebe dois pares de coordenadas e calcule a distância entre os pontos. 

x1 = int(input('Qual o primeiro numeor do primeiro par? '))
y1 = int(input('Qual o segundo numero do primeiro par? '))
x2 = int(input('Qual o primeiro numero do segundo par? '))
y2 = int(input('Qual o segundo numero do segundo par? '))
d = (x2 - x1) ** 2 
d2 = (y2 - y1) ** 2
s1 = (d + d2) ** (1/2)
print(s1)