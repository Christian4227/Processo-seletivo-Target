#Questão 3

lista = [0, 1000, 1500, 2100, 2300, 1900, 0, 0, 1700, 1500,
        1800, 1450, 1700, 0, 0, 1600, 0, 1900, 1600, 1350,
        0, 0, 1800, 1900, 2100, 2300, 550, 0, 0, 1260]
lista2 = [ 1000, 1500, 2100, 2300, 1900, 1700, 1500,
        1800, 1450, 1700, 1600, 1900, 1600, 1350,
        1800, 1900, 2100, 2300, 550, 1260]
        
maxValor = max(lista2)
minValor = min(lista2)
i = 0
soma = 0
dias_folga = 0

while i < len(lista):
    soma += lista[i]
    if lista[i] == 0:
        dias_folga += 1
    i += 1

media = round(soma / (30 - dias_folga))
k = 0
count = 0

while k < len(lista):
    if lista[k] > media:
        count += 1
    k += 1

print('Media = ', media)
print('Dias acima da média: ', count)
print('Valor maior de venda: ', maxValor)
print('Valor menor de venda: ', minValor)