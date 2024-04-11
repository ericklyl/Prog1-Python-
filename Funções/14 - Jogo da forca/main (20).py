def f_cp(a,b):
  if (a == b):
    return True
  else:
    return False
    


def f_rp(let,letr):
  for x in range(len(letr)):
    if(let == letr[x]):
      return True
  return False  
  
  

def f_pr(d):
  for x in range(len(d)):
    print(d[x],end=" ")
  print()
  

def f_vf(le,plv,forc):
  seg2 = ""
  for x in range(len(plv)):
    if (plv[x] == le):
      seg2 += le
    else:
      seg2 += forc[x]
  return seg2


def f_forca(se):
  sef = ""
  for x in range(len(se)):
    sef += "_"
  return sef

 
def main():
  count = 0
  letr = ""
  erro = ""
  jogad = 0
  ganha = False
  
  
  plv = input("Digite a Palavra: ").upper()
  print(plv)
  forc = f_forca(plv)
  f_pr(forc)


  while(count < 6 and not ganha):
    let = input("").upper()
    
    while (f_rp(let,letr)):
      let = input("Tente outra letra: ").upper()
    letr += let
    jogad += 1
    
    if (let in plv):
      forc = f_vf(let,plv,forc) 
      
    else:
      erro += let
      count += 1
    f_pr(forc)
    print(erro)
    ganha = f_cp(forc,plv)
  
  if (ganha):
    print(f'Parabéns, você ganhou com {jogad} jogadas')
    
  else:
    print(f'Que pena, você não acertou a palavra {plv}')
      
if __name__ == "__main__":
  main()