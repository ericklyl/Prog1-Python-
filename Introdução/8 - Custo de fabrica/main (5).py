#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.



def main():
    n1 = int(input())
    cf = n1 + (n1 / 100 * 28) + (n1 / 100 * 45)
    print(cf)
if __name__ == '__main__':
    main()