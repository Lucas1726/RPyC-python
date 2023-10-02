# Autor: Lucas Gonçalves Prado das Neves  
# Série: 06 | Turma: A | Turno: NOTURNO 

import rpyc # biblioteca para Python RPC
from rpyc.utils.server import ThreadedServer

class MyService(rpyc.Service):

    # Descrição: Este método calcula o índice de massa corporal (IMC) dado 
    # o peso e a altura inseridos e retorna uma string indicando o IMC e sua categoria 
    # (magro, normal, sobrepeso, obeso I, obeso II ou obeso III).
    def exposed_imc(self, peso, altura):
        imc = peso / (altura * altura)
        if imc < 18.5:
            return "IMC: " + str(imc) + " - Magreza"
        elif imc >= 18.5 and imc < 24.5:
            return "IMC: " + str(imc) + " - Normal"
        elif imc >= 25 and imc < 29.9:
            return "IMC: " + str(imc) + " - Sobrepeso"
        elif imc >= 30 and imc < 34.9:
            return "IMC: " + str(imc) + " - Obesidade grau I"
        elif imc >= 35 and imc < 39.9:
            return "IMC: " + str(imc) + " - Obesidade grau II"
        else:
            return "IMC: " + str(imc) + " - Obesidade grau III"

    # Descrição: Este método resolve uma equação quadrática com base nos coeficientes de entrada 
    # e retorna uma string descrevendo as raízes da equação. Pode indicar se o coeficiente A é 
    # zero,  o delta é negativo (sem raiz real), o delta é zero (uma raiz real) ou  o delta 
    # é positivo (duas raízes reais).
    def exposed_equacao(self, a, b, c):
        if(a == 0):
            return "Valor do coeficiente A zerado."
        delta = (b * b) - (4 * a * c)
        if delta < 0:
            return "Delta negativo, não possui raízes reais"
        elif delta == 0:
            x = (-b + delta) / (2 * a)
            return "Delta igual a zero, possui uma raiz real: " + str(x)
        else:
            x1 = (-b + delta) / (2 * a)
            x2 = (-b - delta) / (2 * a)
            return "Delta maior que zero, possui duas raízes reais: " + str(x1) + " e " + str(x2)

    # Descrição: Este método verifica se a palavra de entrada é um palíndromo, ou seja. 
    # permanece o mesmo ao ler de trás para frente, ignorando espaços e  maiúsculas e 
    # minúsculas. Retorna uma mensagem indicando se a palavra é um palíndromo ou não.
    def exposed_palindromo(self, palavra):
        palavra = palavra.lower()
        palavra = palavra.replace(" ", "")
        if palavra == palavra[::-1]:
            return f"{palavra} é um palíndromo."
        else:
            return f"{palavra} não é um palíndromo."

    # Esses métodos foram marcados com o decorador exposed, o que significa que eles podem ser 
    # chamados remotamente quando o servidor estiver em execução.

if __name__ == "__main__":
    server = ThreadedServer(MyService, hostname='0.0.0.0', port = 18812)
    print('Servidor online')
    server.start()