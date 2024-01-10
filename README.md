# Poc Don't Be Idle

Um projeto simples para prevenir o estado de inatividade (idle) em seu computador, especialmente útil em ambientes que detectam inatividade...

## Funcionalidades

- **Prevenção de Idle:** Mantém o cursor do mouse em movimento para evitar que o sistema operacional marque o usuário como inativo.
- **Teclas de Atalho:** Possibilidade de criar teclas de atalho no sistema operacional para iniciar ou interromper o script rapidamente.

## Como Usar?

### Pré-requisitos

- Python 3.x
- pip (Python Package Installer)

### Instalação

1. **Clone o Repositório**

    ```bash
    git clone https://github.com/AugustoSavi/PocDontBeIdle.git
    ```

2. **Instale as Dependências**

    Navegue até a pasta do projeto e instale as dependências necessárias:

    ```bash
    cd PocDontBeIdle
    pip3 install -r requirements.txt
    ```

3. **Execute o Programa**

    ```bash
    python3 main.py
    ```

### Criando Teclas de Atalho

#### Windows

1. Crie um atalho para `main.py` clicando com o botão direito no arquivo e selecionando "Criar atalho".
2. Clique com o botão direito no atalho criado e vá em "Propriedades".
3. Na aba "Atalho", no campo "Tecla de atalho", defina a combinação de teclas desejada (por exemplo, Ctrl + Alt + I).
4. Clique em "OK" para salvar.

#### macOS

1. Abra o "Automator" e crie um novo "Serviço".
2. Configure o serviço para executar um script Python e adicione o caminho para `main.py`.
3. Salve o serviço e vá para "Preferências do Sistema" > "Teclado" > "Atalhos".
4. Adicione o serviço criado e defina uma tecla de atalho.

#### Linux

A criação de atalhos pode variar dependendo do ambiente de desktop. Geralmente, você pode ir para as "Configurações do Sistema" e encontrar uma seção para "Teclas de Atalho" ou "Atalhos de Teclado", onde você pode definir um novo atalho para executar `python3 /caminho/para/main.py`.