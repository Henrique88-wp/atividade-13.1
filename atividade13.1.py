# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.

numero = float(input("Digite um numero:"))
def verificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"
print(f"O número é:{verificar_numero(numero)}")