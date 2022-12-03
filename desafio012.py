p = float(input('Digite o preço do produto: '))
pct = p * 5 / 100
print('O valor {} com o desconto de 5% fica {:.2f}'.format(p, (p - pct)))