import subprocess
from datetime import date
from pathlib import Path
from tkinter import messagebox

import mysql.connector as mysql


class Conexao:
    """
    Classe de conexão com o banco de dados MySQL usando singleton.
    """

    _conexao = None  # Atributo Protegido!!!
    __user = None
    __password = None
    __db = None

    @classmethod
    def configurar(cls, host: str, user: str, password: str, db_name: str):
        """
        Configura a conexão com o banco de dados.

        Args:
            host (str): O endereço do host do banco de dados.
            user (str): O nome de usuário para autenticação no banco de dados.
            password (str): A senha para autenticação no banco de dados.
            db_name (str): O nome do banco de dados a ser utilizado.
        """

        if cls._conexao:
            # Fecha a conexão se já existir uma
            cls._conexao.close()

        try:
            cls._conexao = mysql.connect(
                host=host,
                user=user,
                password=password,
                database=db_name,
                autocommit=True,
            )
            cls.__host = host
            cls.__user = user
            cls.__password = password
            cls.__db = db_name
        except Exception as e:
            # Mostra uma mensagem de erro
            messagebox.showerror(title="Erro na conexão com o banco", message=e)

    @classmethod
    def get_conexao(cls):
        """
        Retorna a conexão com o banco de dados.

        Returns:
            Connection: A conexão com o banco de dados.

        Raises:
            Exception: Se a conexão não estiver configurada.
        """
        if cls._conexao is None:
            raise Exception(
                "A conexão não está configurada. Use o método 'configurar' primeiro."
            )
        return cls._conexao

    @classmethod
    def fechar_conexao(cls):
        """
        Fecha a conexão com o banco de dados.
        """
        if cls._conexao:
            cls._conexao.close()
            print("Conexão fechada.")

    @classmethod
    def is_connected(cls) -> bool:
        """
        Verifica se a conexão com o banco de dados está ativa.

        Returns:
            bool: True se a conexão estiver ativa, False caso contrário.
        """
        return cls._conexao is not None and cls._conexao.is_connected()

    @classmethod
    def fazer_backup(cls, local_de_salvamento: Path):
        """
        Faz backup da base de dados.

        Args:
            local_de_salvamento (Path): O caminho do diretório onde o backup será salvo.
        """
        # Obtém a data do dia atual para nomear o arquivo
        data_atual = date.today().strftime("%d_%m_%Y")

        # Concatenar o nome do arquivo com o caminho do diretório
        nome_arquivo = f"backup_{data_atual}.sql"
        caminho_completo = local_de_salvamento / nome_arquivo

        # Cria um arquivo de opções (Método mais seguro)
        arquivo_opcoes = local_de_salvamento / "mysql_options.cnf"
        with arquivo_opcoes.open(mode="w") as arquivo:
            arquivo.write(f"[mysqldump]\nuser={cls.__user}\npassword={cls.__password}")

        try:
            # Construir o comando mysqldump com a opção --defaults-file
            comando_mysqldump = f"mysqldump --defaults-file={arquivo_opcoes} {cls.__db} > {caminho_completo}"

            # Executa no console
            subprocess.run(comando_mysqldump, shell=True, check=True)

            # Exibe uma mensagem de sucesso
            messagebox.showinfo(
                "Backup Concluído",
                f"Backup realizado com sucesso em {caminho_completo}",
            )

        except Exception as e:
            # Exibe uma mensagem de erro
            messagebox.showerror("Erro ao fazer backup", f"Erro durante o backup: {e}")

        finally:
            # Remove o arquivo de opções após o uso
            arquivo_opcoes.unlink()
