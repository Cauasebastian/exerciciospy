# 1. Soma de todos os números ímpares múltiplos de três entre 1 e 500
print("Soma de todos os números ímpares múltiplos de três entre 1 e 500")
soma = sum(i for i in range(1, 501) if i % 2 != 0 and i % 3 == 0)
print(f"A soma de todos os números ímpares múltiplos de três entre 1 e 500 é: {soma}")
print()

# 2. Menor e maior altura do grupo de 15 pessoas
print("Menor e maior altura do grupo de 15 pessoas")
alturas = [float(input(f"Digite a altura da pessoa {i+1}: ")) for i in range(15)]
menor_altura = min(alturas)
maior_altura = max(alturas)
print(f"A menor altura do grupo é: {menor_altura:.2f} metros")
print(f"A maior altura do grupo é: {maior_altura:.2f} metros")
print()

# 3. Média aritmética, quantidade de valores positivos, negativos e percentuais
print("Média aritmética, quantidade de valores positivos, negativos e percentuais")
valores = []
while True:
    valor = float(input("Digite um valor (ou um número negativo para encerrar): "))
    if valor < 0:
        break
    valores.append(valor)

if valores:
    media = sum(valores) / len(valores)
    positivos = [v for v in valores if v > 0]
    negativos = [v for v in valores if v < 0]
    qtd_positivos = len(positivos)
    qtd_negativos = len(negativos)
    pct_positivos = (qtd_positivos / len(valores)) * 100
    pct_negativos = (qtd_negativos / len(valores)) * 100

    print(f"Média aritmética: {media:.2f}")
    print(f"Quantidade de valores positivos: {qtd_positivos}")
    print(f"Quantidade de valores negativos: {qtd_negativos}")
    print(f"Percentual de valores positivos: {pct_positivos:.2f}%")
    print(f"Percentual de valores negativos: {pct_negativos:.2f}%")
    print()

# 4. Contagem de números em intervalos específicos
print("Contagem de números em intervalos específicos")
contagem = [0, 0, 0, 0]  # [0-25], [26-50], [51-75], [76-100]
while True:
    numero = int(input("Digite um número (ou um número negativo para encerrar): "))
    if numero < 0:
        break
    if 0 <= numero <= 25:
        contagem[0] += 1
    elif 26 <= numero <= 50:
        contagem[1] += 1
    elif 51 <= numero <= 75:
        contagem[2] += 1
    elif 76 <= numero <= 100:
        contagem[3] += 1

print(f"Quantidade nos intervalos:")
print(f"[0-25]: {contagem[0]}")
print(f"[26-50]: {contagem[1]}")
print(f"[51-75]: {contagem[2]}")
print(f"[76-100]: {contagem[3]}")
print()

# 5. Contagem de pares, ímpares, média de pares e média geral
print("Contagem de pares, ímpares, média de pares e média geral")
pares = []
impares = []
while True:
    numero = int(input("Digite um número positivo (ou 0 para encerrar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

if pares or impares:
    media_pares = sum(pares) / len(pares) if pares else 0
    media_geral = (sum(pares) + sum(impares)) / (len(pares) + len(impares))

    print(f"Quantidade de números pares: {len(pares)}")
    print(f"Quantidade de números ímpares: {len(impares)}")
    print(f"Média dos valores pares: {media_pares:.2f}")
    print(f"Média geral dos números: {media_geral:.2f}")
    print()

# 6. Números ímpares entre 100 e 200
print("Números ímpares entre 100 e 200")
impares = [i for i in range(101, 200, 2)]
print("Números ímpares entre 100 e 200:", impares)
print()

# 7. Tabuada de N (de 1 a 10)
print("Tabuada de N (de 1 a 10)")
N = int(input("Digite um número de 1 a 10 para ver a tabuada: "))
if 1 <= N <= 10:
    for i in range(11):
        print(f"{i} x {N} = {i * N}")
print()    

# 8. Sequência em Progressão Aritmética (PA) de 10 valores
print("Sequência em Progressão Aritmética (P.A.) de 10 valores")
A = int(input("Digite o valor inicial (A): "))
R = int(input("Digite a razão (R): "))
pa = [A + R * i for i in range(10)]
print("Sequência em P.A.:", pa)
print()

# 9. Sequência em Progressão Geométrica (PG) de 10 valores
print("Sequência em Progressão Geométrica (P.G.) de 10 valores")
A = int(input("Digite o valor inicial (A): "))
R = int(input("Digite a razão (R): "))
pg = [A * (R ** i) for i in range(10)]
print("Sequência em P.G.:", pg)
print()

# 10. Sequência de valores do fatorial de A e seu resultado
print("Sequência de valores do fatorial de A e seu resultado")
A = int(input("Digite o valor de A para calcular A!: "))
fatorial = 1
sequencia = []
for i in range(A, 0, -1):
    fatorial *= i
    sequencia.append(i)

print(f"{A}! = {' x '.join(map(str, sequencia))} = {fatorial}")
print()
