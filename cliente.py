# Autor: Lucas Gonçalves Prado das Neves  
# Série: 06 | Turma: A | Turno: NOTURNO 

import rpyc # biblioteca para Python RPC

conn = rpyc.connect('localhost', 18812)

try:
    # Método 1: IMC
    peso_str  = input('Digite seu peso: ')
    altura_str  = input('Digite sua altura: ')

    peso_str = peso_str.replace(',', '.')
    altura_str = altura_str.replace(',', '.')

    peso = float(peso_str)
    altura = float(altura_str)

    result = conn.root.exposed_imc(peso, altura)
    print(result)

    # Método 2: Equação quadrática
    a_str = input('Digete um valor para a: ')
    b_str = input('Digete um valor para b: ')
    c_str = input('Digete um valor para c: ')

    a_str = a_str.replace(',', '.')
    b_str = b_str.replace(',', '.')
    c_str = c_str.replace(',', '.')

    a = float(a_str)
    b = float(b_str)
    c = float(c_str)

    result = conn.root.exposed_equacao(a, b, c)
    print(result)

    # Método 3: Palíndromo
    palavra = input('Digete uma palavra: ')
    result = conn.root.exposed_palindromo(palavra)
    print(result)

finally:
    conn.close() # Fecha a conexão com o servidor
