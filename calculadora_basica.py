def input_valores():
    'Recebe dois valores inteiros do usuário'

    numero1 = int(input('Digite o primeiro valor: '))
    numero2 = int(input('Digite o segundo valor: '))

    return numero1, numero2

#  SOMA
numero1, numero2 = input_valores()
def soma(numero1:int, numero2:int) -> int:
    'Retorna a soma entre dois valores'

    resultado = numero1 + numero2
    print(f'A soma entre {numero1} e {numero2} é igual a {resultado}')

# SUBTRAÇÃO
def subtracao(numero1:int, numero2:int) -> int:
    'Retorna a subtração entre dois valores'

    resultado = numero1 - numero2
    print(f'A subtração entre {numero1} e {numero2} é igual a {resultado}')

# MULTIPLICAÇÃO
def multiplicacao(numero1:int, numero2:int) -> int:
    'Retorna a multiplicação entre dois valores'

    resultado = numero1 * numero2
    print(f'A multiplicação entre {numero1} e {numero2} é igual a {resultado}')

#DIVISÃO
def divisao(numero1:int, numero2:int) -> int:
    'Retorna a divisão entre dois valores'

    resultado = numero1 / numero2
    print(f'A divisão entre {numero1} e {numero2} é igual a {resultado}')
