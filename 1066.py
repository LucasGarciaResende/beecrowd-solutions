par, imp, pos, neg = 0, 0, 0, 0
for i in range(0, 5):
    num = int(input())
    if num % 2 == 0:
        par += 1
    else:
        imp += 1
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
print(f'{par} valor(es) par(es)\n'
      f'{imp} valor(es) impar(es)\n'
      f'{pos} valor(es) positivo(s)\n'
      f'{neg} valor(es) negativo(s)')
