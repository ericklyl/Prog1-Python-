def f_somada(x,rodadas):
	if rodadas==1:
		if (x==7 or x==11):
			result = f"NATURAL!VOCÊ GANHOU! \n JOGADAS = {rodadas}"
			return result
		if (x==2 or x==3 or x==12):
			result = f"CRAPS!VOCÊ PERDEU! \n JOGADAS = {rodadas}"
			return result
		if (x>3 or x>7):
			return x
	else:
		if (x!=7):
			return x
		else:
			result= f"VOCÊ PERDEU! \n JOGADAS = {rodadas}"
			return result

def main():
	x=int(input()) 
	rodadas=1
	print (x)
	ponto = f_somada(x,rodadas)
	Checkada=0
	
	if str(type(ponto))=="<class 'str'>":
		print (ponto)
	
	else:
		while((ponto!=Checkada) and ( isinstance(Checkada,str)==False)):
			rodadas=rodadas+1
			x=int(input())
			print (x)
			Checkada = f_somada(x,rodadas)
	
	if (str(type(Checkada))=="<class 'str'>" and rodadas>1):
		print (Checkada)
	
	elif (str(type(Checkada))!="<class 'str'>" and rodadas>1):
		print(f"VOCÊ GANHOU \n JOGADAS = {rodadas}")
	return 0

if __name__ == '__main__':
	main()