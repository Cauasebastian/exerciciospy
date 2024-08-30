# 1. Verificar se a soma de A + B é menor que C
print("Verificar se o valor de A + B é menor que C")
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A + B < C:
    print("A soma de A + B é menor que C.")
else:
    print("A soma de A + B não é menor que C.")

# 2. Solicitar tempo de casada se for mulher e casada
print("Verificar se é mulher casada e solicitar tempo de casamento")
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M/F): ").upper()
estado_civil = input("Digite seu estado civil: ").upper()

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (anos): "))
    print(f"Tempo de casada: {tempo_casada} anos.")
else:
    print("Não é mulher casada.")

# 3. Verificar se um número é par ou ímpar
print("Verificar se um número é par ou ímpar")
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 4. Soma ou multiplicação de A e B, com resultado em C
print("Calcular a soma ou multiplicação de A e B")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A == B:
    C = A + B
else:
    C = A * B

print(f"O valor de C é: {C}")

# 5. Dobro ou triplo de um número
print("Calcular o dobro ou triplo de um número")
numero = float(input("Digite um número: "))

if numero > 0:
    resultado = numero * 2
else:
    resultado = numero * 3

print(f"O resultado é: {resultado}")

# 6. Verificar se dois valores booleanos são ambos verdadeiros ou falsos
print("Verificar se dois valores lógicos são ambos verdadeiros ou falsos")
valor1 = bool(int(input("Digite o primeiro valor lógico (0 ou 1): ")))
valor2 = bool(int(input("Digite o segundo valor lógico (0 ou 1): ")))

if valor1 and valor2:
    print("Ambos são VERDADEIROS.")
else:
    print("Ambos são FALSOS.")

# 7. Somar 5 se par ou somar 8 se ímpar
print("Somar 5 se o número for par ou somar 8 se o número for ímpar")
variavel = int(input("Digite um número: "))

if variavel % 2 == 0:
    resultado = variavel + 5
else:
    resultado = variavel + 8

print(f"O resultado é: {resultado}")

# 8. Mostrar três valores inteiros em ordem decrescente
print("Mostrar três valores inteiros em ordem decrescente")
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

valores = [valor1, valor2, valor3]
valores.sort(reverse=True)

print(f"Valores em ordem decrescente: {valores}")

# 9. Calcular o peso ideal com base na altura e sexo
print("Calcular o peso ideal com base na altura e sexo")
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M/F): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7

print(f"O peso ideal é: {peso_ideal:.2f} kg")

# 10. Calcular o IMC e mostrar a condição de peso
print("Calcular o IMC e mostrar a condição de peso")
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    condicao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    condicao = "Peso normal"
elif 25 <= imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"

print(f"O IMC é: {imc:.2f}. Condição: {condicao}")

# 11. Calcular o valor a ser pago por um produto com base na condição de pagamento
print("Calcular o valor a ser pago por um produto com base na condição de pagamento")
preco_etiqueta = float(input("Digite o preço do produto: "))
codigo_pagamento = int(input("Digite o código da condição de pagamento (1-4): "))

if codigo_pagamento == 1:
    valor_final = preco_etiqueta * 0.90
elif codigo_pagamento == 2:
    valor_final = preco_etiqueta * 0.85
elif codigo_pagamento == 3:
    valor_final = preco_etiqueta
elif codigo_pagamento == 4:
    valor_final = preco_etiqueta * 1.10

print(f"O valor a ser pago é: R$ {valor_final:.2f}")

# 12. Calcular média de aproveitamento e atribuir conceito
print("Calcular média de aproveitamento e atribuir conceito")
numero_identificacao = int(input("Digite o número de identificação do aluno: "))
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media_exercicios = float(input("Digite a média dos exercícios: "))

media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

if media_aproveitamento >= 90:
    conceito = "A"
elif 75 <= media_aproveitamento < 90:
    conceito = "B"
elif 60 <= media_aproveitamento < 75:
    conceito = "C"
elif 40 <= media_aproveitamento < 60:
    conceito = "D"
else:
    conceito = "E"

status = "Aprovado" if conceito in ["A", "B", "C"] else "Reprovado"

print(f"Número de Identificação: {numero_identificacao}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos Exercícios: {media_exercicios}")
print(f"Média de Aproveitamento: {media_aproveitamento:.2f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")
