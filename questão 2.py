# Questão 2 - Sequência de Fibonacci

lista = []
ant1 = 0
ant2 = 1
i = 0
soma = 0
lista.append(ant1)
lista.append(ant2)

while i < 10:
    soma = ant1 + ant2
    ant1 = ant2
    ant2 = soma
    lista.append(soma)
    soma = 0
    i += 1
print(lista)

entr = int(input('Digite um número para verificar se está na sequência de Fibonacci: '))
if entr > 34:
    print('Limitamos a quantidade de termos da sequência de Fibonacci em 10 termos.')
else:
    if entr in lista:
        print('O número que você digitou está na sequência de Fibonacci.')
    else:
        print('O número que você digitou não está na sequência de Fibonacci.')