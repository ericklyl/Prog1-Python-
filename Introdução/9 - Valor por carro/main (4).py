#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

n1 = int(input('numero de carros vendidos? '))
n2 = int(input('valor das vendas? '))
n3 = int(input('qual o salario fixo? '))
n4 = int(input("qual o valor que ele recebe por carro? "))
sc = n3 + (n4 * n1) + (5/100 * n2)
print(sc)
