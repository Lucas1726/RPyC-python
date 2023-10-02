Para testar o script Python chamado server.py e client.py, você pode seguir estas etapas gerais:

1° - Certifique-se de ter o Python instalado: Você pode fazer isso executando python --version ou python3 --version no seu terminal. Se o Python não estiver instalado, você precisará instalá-lo primeiro. (https://www.python.org/downloads/)

![image](https://github.com/Lucas1726/RPyC-python/assets/92900328/39cab9a9-735c-4ae8-8571-4b9ef4c9af5e)

2° Você pode criar um ambiente virtual para manter essas dependências isoladas do seu sistema global (é uma prática recomendada). Siga estas etapas:

- Linux/Mac: (source venv/bin/activate)
- Windows (PowerShell): (venv\Scripts\Activate.ps1)

![image](https://github.com/Lucas1726/RPyC-python/assets/92900328/9468e949-e6ef-4510-9da9-2d4fe1b5b8b8)

3° - Instale os pacotes necessário:

- pip install requests

![image](https://github.com/Lucas1726/RPyC-python/assets/92900328/05cf26ca-6e2c-4eb5-a3f7-02c6a0ff601c)

- pip install rpyc

![image](https://github.com/Lucas1726/RPyC-python/assets/92900328/5a034785-f20c-4dfb-9ad0-44b67343ba91)

4° - Verifique onde está localizado os scipts server.py e client.py. De preferência deixe nesta pasta C:\Users\nome_do_computador
- "C:" é a letra que representa a unidade principal do disco rígido do computador, onde a maior parte dos arquivos do sistema e programas está armazenada.
- "Users" é a pasta que contém os perfis de todos os usuários do computador.
- "nome_do_computador" é o nome de usuário específico, e dentro desta pasta estão localizados os documentos, imagens, músicas e outros arquivos pessoais pertencentes ao usuário "nome_do_computador".

5° - Execute o servidor usando o seguinte comando:
- python server.py

![image](https://github.com/Lucas1726/RPyC-python/assets/92900328/a4e8fdaa-27f0-4cf3-bb82-ee1fe77f6916)

6° - Em um programa diferente de onde está sendo executado o servidor. Execute o cliente usando o seguinte comando para ativar o client.py:
- python client.py

![image](https://github.com/Lucas1726/RPyC-python/assets/92900328/0bee8733-05be-42c8-b40c-07592bc767f9)

OBS: É necessário ativar o ambiente virtual na outra aba do programa novamente, NÃO é necessário fazer a importação dos pacotes, apenas ativar o ambiente virtual.

Agora que o cliente está em execução, ele se conectará automaticamente ao servidor e fará chamadas RPC para os métodos disponíveis no servidor. No seu caso, o cliente faz três chamadas RPC para os métodos exposed_imc, exposed_equacao, e exposed_palindromo.

- Para calcular o IMC (Índice de Massa Corporal), o cliente envia os valores de peso e altura para o servidor, que retorna o resultado do cálculo do IMC e a mensagem de classificação.
- Para calcular uma equação do segundo grau, o cliente envia os coeficientes a, b e c para o servidor, que retorna as raízes da equação (se houver).
- Para verificar se uma palavra é um palíndromo, o cliente envia a palavra para o servidor, que verifica se ela é um palíndromo e retorna uma mensagem correspondente.

7 - Visualizar os Resultados

Os resultados das chamadas RPC feitas pelo cliente serão impressos no terminal onde o cliente está em execução. Você verá a saída do servidor para cada uma das chamadas.

![image](https://github.com/Lucas1726/RPyC-python/assets/92900328/39d1b689-c7d5-417c-9be0-5aad6bd90ce8)

8 - Encerrar a Execução

Depois de obter os resultados ou quando você não precisar mais dos serviços, você pode simplesmente fechar o terminal do cliente para encerrar a execução do cliente. O servidor continuará em execução até que você o encerre manualmente no terminal do servidor pressionando Ctrl+C.

Lembre-se de que é importante manter o servidor em execução enquanto você estiver usando o cliente, caso contrário, o cliente não conseguirá se conectar ao servidor.

Espero ter ajudado!
