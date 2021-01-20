L=[]
x = 1
while True:
    n = str(input("Digite a %sº posição ou digite sair para sair da aplicação: "% x))
    if n == "sair":
        break
    else:
        L.append(n)
        x = x + 1
escolhido = int(input("Digite número de acordo com a posição: "))
print(L[escolhido-1])
