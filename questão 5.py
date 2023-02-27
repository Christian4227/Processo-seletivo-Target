entr = input('Digite uma palavra para inverter.')
i = 0
pal_inv = ''
comp = len(entr)

while i < comp:
    pal_inv += entr[comp - 1 - i]
    i += 1
print(pal_inv)