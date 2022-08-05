ant = 1
suc = 1
valor = int(input("Digite um valor"))
cont = 0
soma = 0
lista = []
while True:
    if cont <= valor:
        soma = ant + suc
        ant = suc
        suc = soma
        lista.append(ant)
        cont += 1
    else:
        break
print(lista)