dias = int(input())
anos = dias // 365
if anos > 0:
    dias -= (365 * anos)
meses = dias // 30
if meses > 0:
    dias -= (30 * meses)
print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')
