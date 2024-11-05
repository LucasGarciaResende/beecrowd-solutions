valor = float(input())
valor = int(valor * 100)

moedas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
quantidade = 0
quantidades = []
for moeda in moedas:
    quantidade = valor // moeda
    quantidades.append(quantidade)
    valor %= moeda

print("NOTAS:\n"
      f"{quantidades[0]} nota(s) de R$ 100.00\n"
      f"{quantidades[1]} nota(s) de R$ 50.00\n"
      f"{quantidades[2]} nota(s) de R$ 20.00\n"
      f"{quantidades[3]} nota(s) de R$ 10.00\n"
      f"{quantidades[4]} nota(s) de R$ 5.00\n"
      f"{quantidades[5]} nota(s) de R$ 2.00\n"
      f"MOEDAS:\n"
      f"{quantidades[6]} moeda(s) de R$ 1.00\n"
      f"{quantidades[7]} moeda(s) de R$ 0.50\n"
      f"{quantidades[8]} moeda(s) de R$ 0.25\n"
      f"{quantidades[9]} moeda(s) de R$ 0.10\n"
      f"{quantidades[10]} moeda(s) de R$ 0.05\n"
      f"{quantidades[11]} moeda(s) de R$ 0.01")