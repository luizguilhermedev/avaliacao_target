
# Avaliação Técnica Target Sistemas para vaga de Estágio 2024

"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);
"""
# Solução

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA = SOMA + K

print(f"Valor da soma é: {SOMA}")
# >> 91


"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma
dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""
# Solução

def fibonacci(number: int|float):
    """
    Função que verifica se um número pertence ou não a sequência de Fibonacci.
    Imprime uma lista com a sequência de Fibonacci até o número informado.
    
    Parâmetros:
    number (int|float): Número a ser verificado.
    
    Retorno:
    (bool, list): Retorna um booleano indicando se o número pertence ou não a sequência e uma lista com a sequência de Fibonacci.
    
    Exemplo de uso:
    pertence, sequencia = fibonacci(number)
    if pertence:
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} não pertence à sequência de Fibonacci.")
    
    print(f"Sequência Fibonacci até o número informado: {sequencia}")
    
    Testes:
    fibonacci(0) -> (True, [0])
    fibonacci(1) -> (True, [0, 1])
    """
    a, b = 0, 1
    fib_sequence = [a, b] # Lista para armazenar a sequência

    while b < number:
        a, b = b, a + b
        fib_sequence.append(b)
    if b == number:
        return True, fib_sequence # Retorna a lista com a sequência de Fibonacci
    else:
        return False, fib_sequence # Retorna a lista vazia
    
number = int(input("Digite um número: "))
pertence, sequencia = fibonacci(number)
if fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} não pertence à sequência de Fibonacci.")

print(f"Sequência Fibonacci até o número informado: {sequencia}")


"""
3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____

"""

# Solução

# a) 1, 3, 5, 7, 9 A lógica é que adicionamos 2 a cada termo

# b) 2, 4, 8, 16, 32, 64, 128 A lógica é que multiplicamos cada termo por 2

# c) 0, 1, 4, 9, 16, 25, 36, 49 Sequẽncia que representa o quadrado de números Naturais

# d) 4, 16, 36, 64, 100 Sequẽncia que representa o quadrado de números Inteiros pares(2,4,6,8,10)

# e) 1, 1, 2, 3, 5, 8, 13 A lógica é que somamos cada termo com seu anterior

# f) 2,10, 12, 16, 17, 18, 19 adicionar números pares e ímpares sequencialmente


"""
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
"""

# Solução

# Ligamos um dos interruptores e esperamos alguns minutos.
# Desligamos o interruptor que acabamos de ligar e, simultaneamente, ligamos outro interruptor que não foi usado anteriormente.
# Vamos até a sala onde estão as lâmpadas.
# Se uma lâmpada estiver acesa, isso significa que o interruptor que ligamos primeiro controla essa lâmpada.
# Se outra lâmpada estiver acesa, isso significa que o interruptor que ligamos por último controla essa lâmpada.
# Se nenhuma lâmpada estiver acesa, isso significa que o interruptor restante controla essa lâmpada.

"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""

# Solução


def invert_string(string: str):
    """
    Função que inverte os caracteres de uma string.

    Parâmetros:
    string (str): String a ser invertida.

    Retorno:
    (str): String invertida.

    Exemplo de uso:
    inverted_string = invert_string(string)
    print(f"String invertida: {inverted_string}")

    Testes:
    invert_string("Hello World") -> "dlroW olleH"
    invert_string("Python") -> "nohtyP"
    """
    inverted_string = ""
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

string = input("Digite uma string: ")
inverted_string = invert_string(string)
print(f"String invertida: {inverted_string}")

