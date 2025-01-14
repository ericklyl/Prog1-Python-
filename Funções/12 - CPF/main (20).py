def f_digitoVerificador(c,m):
  term = 0
  for i in range(len(c)):
    term += int(c[i]) * m
    m -= 1
  resto = term % 11
  if (resto < 2):
    return 0
  else:
    return 11-resto

def f_apenasNumeros(c):
  c2 = ""
  i = 0
  cont = 0
  while cont < 9:
    if (c[i] != "."):
      c2 += c[i]
      cont += 1
    i += 1
  return c2

def f_validador(c):
  cpf = c
  c = f_apenasNumeros(c)
  dv1 = f_digitoVerificador(c,10)
  c += str(dv1)
  dv2 = f_digitoVerificador(c,11)
  dv = str(dv1)+str(dv2)
  if (cpf[12:] == dv):
    return True
  else:
    return False


def main():
  cpf = input("CPF")
  if (f_validador(cpf)):
    print(" VÁLIDO")
  else:
    print(" INVÁLIDO")
  return 0

if __name__ == "__main__":
  main()