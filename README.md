# RPC Python - Cálculo de IMC, Equação Quadrática e Palíndromo

## Sobre o Projeto
Este projeto consiste em uma aplicação cliente-servidor utilizando **RPC (Remote Procedure Call)** com a biblioteca **rpyc**. O servidor disponibiliza três funcionalidades principais:

1. **Cálculo do IMC (Indice de Massa Corporal)**
2. **Resolução de uma Equação Quadrática**
3. **Verificação se uma palavra é um Palíndromo**

O cliente se conecta ao servidor e solicita a execução desses métodos remotamente.

---

## Tecnologias Utilizadas
- **Python**
- **Biblioteca rpyc**

---

## Como Executar o Projeto
### 1. Instalar Dependências
Antes de executar o projeto, certifique-se de ter o **Python** instalado e a biblioteca **rpyc** instalada. Caso não tenha o `rpyc`, instale com:

```sh
pip install rpyc
```

### 2. Iniciar o Servidor
Execute o seguinte comando no terminal para iniciar o servidor:

```sh
python server.py
```

Se tudo estiver correto, a seguinte mensagem será exibida:
```
Servidor online
```

### 3. Executar o Cliente
Abra outro terminal e execute o cliente para interagir com o servidor:

```sh
python cliente.py
```

O cliente solicitará entradas do usuário para cada uma das três funcionalidades:
- Digitar peso e altura para calcular o IMC.
- Digitar os coeficientes `a`, `b` e `c` para resolver uma equação quadrática.
- Digitar uma palavra para verificar se é um palíndromo.

---

## Estrutura do Código

### `server.py`
O servidor define três métodos expostos via RPC:
- `exposed_imc(peso, altura)`: Calcula o IMC e retorna a classificação correspondente.
- `exposed_equacao(a, b, c)`: Resolve uma equação quadrática e retorna as raízes.
- `exposed_palindromo(palavra)`: Verifica se uma palavra é um palíndromo.

O servidor é iniciado na porta `18812` e escuta requisições do cliente.

### `cliente.py`
O cliente se conecta ao servidor na porta `18812` e interage com o usuário para coletar entradas, chamando os métodos remotos expostos pelo servidor.

---

## Autor
**Lucas Gonçalves Prado das Neves**  
Série: 06 | Turma: A | Turno: NOTURNO

---

## Licença
Este projeto é de uso educacional e pode ser modificado e distribuído livremente.

