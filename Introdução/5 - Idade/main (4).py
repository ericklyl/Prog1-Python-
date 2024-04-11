anos = int(input('Digite os anos? '))
meses = int(input('Digite os meses? '))
dias = int(input('Digite os dias? '))
v1 = anos * 365
v2 = meses * 30
v3 = (dias + v1 + v2)
print('A idade dessa pessoa em dias é ',v3)