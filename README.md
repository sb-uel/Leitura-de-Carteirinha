# Leitura de Carteirinha

Bem-vindo ao projeto de desenvolvimento do Sistema de Leitura de Carteirinha para o IEEE na Universidade Estadual de Londrina (UEL). Este projeto tem como objetivo principal facilitar a organização e registro de presenças dos membros do IEEE na UEL.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos


**Instalando o Python**

Certifique-se de ter o [Python3 instalado](https://realpython.com/installing-python/) em sua máquina.

Dependendo da sua instalação, você pode ter acesso ao interpretador Python3 executando `python` ou `python3`. O mesmo vale para o gerenciador de pacotes pip, você pode acessá-lo executando `pip` ou `pip3`.

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

Certifique-se também de ter o [MySQL](https://dev.mysql.com/downloads/installer/) instalado, além disso para funcionar corretamente é necessário que tenha o `mysqldump` configurado nas variáveis de ambiente do sistema no PATH.
Você pode verificar a configuração executando o comando:
```bash
mysqldump --version
```

**Fontes Customizadas**

O projeto usa as fontes [Horta](https://fontmeme.com/fontes/fonte-horta/) e a [Courierprime](https://fonts.google.com/specimen/Courier+Prime) portanto para visualizar o design do projeto corretamente é necessário instalá-las manualmente

### 🔧 Instalação

**Instalando dependências**
Instale todas as dependências necessárias para o projeto executando:

```bash
pip install -r requirements.txt
```

**Executando o programa**
Para executar o programa utilize o seguinte comando no diretório raiz do projeto:  
OBS: Se estiver usando um ambiente virtual será necessário ativá-lo sempre que for executar o programa
```bash
python main.py
```

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem de programação
* [MySQL](https://www.mysql.com/) - Sistema de gerenciamento de banco de dados relacional (SGBDR)
* [Tkinter](https://docs.python.org/pt-br/3/library/tkinter.html) - Biblioteca usada para criação das interfaces

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](https://github.com/sb-uel/Leitura-de-Carteirinha/blob/main/LICENSE) para detalhes.

