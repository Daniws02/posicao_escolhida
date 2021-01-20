L=[]
x = 1
while True:
    n = str(input("Digite a %sº posição ou 0 para sair: "% x))
    if n == "s":
        break
    else:
        L.append(n)
        x = x + 1
escolhido = int(input("Digite número de acordo com a posição: "))
print(L[escolhido-1])
