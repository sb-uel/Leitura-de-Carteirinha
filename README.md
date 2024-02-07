# Leitura de Carteirinha

Bem-vindo ao projeto de desenvolvimento do Sistema de Leitura de Carteirinha para o IEEE na Universidade Estadual de Londrina (UEL). 
Este projeto tem como objetivo principal facilitar a organização e registro de presenças dos membros do IEEE na UEL.

## 🚀 Começando

Estas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

**Instalando o Python**

Certifique-se de ter o [Python3 instalado](https://realpython.com/installing-python/) em sua máquina.

Dependendo da sua instalação, você pode ter acesso ao interpretador Python3 executando `python` ou `python3`. 
O mesmo vale para o gerenciador de pacotes pip, você pode acessá-lo executando `pip` ou `pip3`.

Você pode ver a versão do seu Python executando:

```bash
python --version
```

Observe que neste repositório sempre que você vê o `python`, será assumido que é o Python **3**.
Você pode usar a biblioteca padrão do Python [venv](https://docs.python.org/3/library/venv.html)
para criar ambientes virtuais e ter o Python, pip e todos os outros pacotes a serem instalados
 a partir do diretório local do projeto para evitar mexer com pacotes externos ou do sistema.

Você pode criar um ambiente virtual executando o seguinte comando:

```bash
python -m venv venv
```

**Instalando MySQL**

Certifique-se de ter o [MySQL](https://dev.mysql.com/downloads/installer/) instalado. É necessário que o `mysqldump` esteja configurado nas variáveis de ambiente do sistema no PATH. Você pode verificar a configuração executando o comando:

```bash
mysqldump --version
```

**Fontes Customizadas**

O projeto utiliza as fontes [Horta](https://fontmeme.com/fontes/fonte-horta/) e [Courierprime](https://fonts.google.com/specimen/Courier+Prime), portanto, para visualizar o design do projeto corretamente, é necessário instalá-las manualmente.

### 🔧 Instalação

**Instalando Dependências**

Instale todas as dependências necessárias para o projeto executando:

```bash
pip install -r requirements.txt
```

**Criando o Esquema do Banco de Dados**

**Com o MySQL Workbench:**

Sincronize seu servidor local com o modelo fornecido em [Carteirinha.mwb](https://github.com/sb-uel/Leitura-de-Carteirinha/blob/main/db/Carteirinha.mwb) usando o MySQL Workbench.

**Sem o MySQL Workbench:**

Se você não possui o MySQL Workbench instalado, pode criar o esquema do banco de dados executando o script SQL diretamente no terminal. Certifique-se de estar logado no MySQL antes de prosseguir.

1. Baixe o script SQL em [Carteirinha.sql](https://github.com/sb-uel/Leitura-de-Carteirinha/blob/main/db/Carteirinha.sql).

2. No terminal, navegue até o diretório onde você baixou o script.

3. Certifique-se de estar logado no MySQL.

    ```bash
    mysql -u seu_usuario -p
    ```

   Substitua `seu_usuario` pelo nome do seu usuário MySQL. O sistema solicitará a senha após executar esse comando.

4. Execute o seguinte comando para aplicar o esquema ao seu banco de dados local:

    ```bash
    source Caminho/Do/Arquivo/Carteirinha.sql;
    ```

   Substitua "Caminho/Do/Arquivo/" pelo caminho real onde o arquivo `Carteirinha.sql` está localizado no seu sistema.

**Executando o Programa**

Para executar o programa, utilize o seguinte comando no diretório raiz do projeto:

OBS: Se estiver usando um ambiente virtual, será necessário ativá-lo sempre que for executar o programa.

```bash
python main.py
```

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem de programação
* [MySQL](https://www.mysql.com/) - Sistema de gerenciamento de banco de dados relacional (SGBDR)
* [Tkinter](https://docs.python.org/pt-br/3/library/tkinter.html) - Biblioteca usada para criação das interfaces
* [TkDesigner](https://github.com/ParthJadhav/Tkinter-Designer) - Biblioteca usada inicialmente na criação de interfaces usando o Figma para gerar códigos em tkinter

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](https://github.com/sb-uel/Leitura-de-Carteirinha/blob/main/LICENSE) para detalhes.

