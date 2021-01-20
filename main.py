L=[]
x = 1
while True:
    n = int(input("Digite a %dº posição ou 0 para sair: "% x))
    if n == 0:
        break
    else:
        L.append(n)
        x = x + 1
escolhido = int(input("Digite número de acordo com a posição: "))
print(L[escolhido-1])