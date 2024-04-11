def f_bissexto(ano):
  if (ano % 4 == 0):
    if (ano % 100 != 0):
      return f'É BISSEXTO'
    else:
      if (ano % 400 == 0):
        return f'É BISSEXTO'
  return f'NÃO É BISSEXTO'


def main():
  ano = int(input('Qual o ano? '))
  f = f_bissexto(ano)
  print(f)


if __name__=='__main__':
  main()