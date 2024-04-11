#Faça um programa em Python3 para resolver o seguinte problema:

#Deseja-se fazer um levantamento a respeito da ausência de alunos à primeira prova de Programação de Computadores para as N turmas de existentes no Ifes. O valor de N é fornecido pelo usuário. O valor de N (quantidade de turmas) é o primeiro dado fornecido ao usuário.

def main():
  #turmas = int(input())
  countTA = 0
  countTB = 0
  countTC = 0
  countTD = 0
  aus = 0
  maior = 0
  menor = 500
  count20 = 0
  turmas = int(input())
  for c in range(turmas):
    countA = 0
    tipo = input()
    qntdalunos = int(input())
    for i in range(qntdalunos):
      matricula = input()
      frequencia = input()
      
      if (frequencia == 'A'):
          countA += 1
    aus = countA * 100 / qntdalunos
          #print(f'{aus:.2f}')

    if (aus < menor):
      menor = aus
      namemenor = tipo
    elif (aus > maior):
      maior = aus
      namemaior = tipo
        #print(f'{aus:.2f}')
    if (aus > 20):
      count20 += 1
    print(f'TURMA = {tipo} AUSENCIA = {aus:.2f} %')
  print(f'TURMA COM MAIOR % DE AUSENCIA= {namemaior} AUSENCIA= {maior:.2f}%')
  print(f'TURMA COM MENOR % DE AUSENCIA= {namemenor} AUSENCIA= {menor:.2f}%')

  print(f'{count20} TURMAS COM % DE AUSENCIA SUPERIOR A 20%')
if __name__=="__main__":
  main()