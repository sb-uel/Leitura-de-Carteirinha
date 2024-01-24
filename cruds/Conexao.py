import subprocess
from datetime import date
from pathlib import Path
from tkinter import messagebox

import mysql.connector as mysql


# Usa o padrão de projeto Singleton para a conexão do banco de dados
class Conexao:
    _conexao = None  # Atributo Protegido!!!
    __user = None
    __password = None
    __db = None

    @classmethod
    def configurar(cls, host, user, password, db_name):
        # Certifique-se de fechar a conexão existente, se houver
        if cls._conexao:
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
        if cls._conexao is None:
            raise Exception(
                "A conexão não está configurada. Use o método 'configurar' primeiro."
            )
        return cls._conexao

    @classmethod
    def fechar_conexao(cls):
        if cls._conexao:
            cls._conexao.close()
            print("Conexão fechada.")

    @classmethod
    def is_connected(cls):
        return cls._conexao is not None and cls._conexao.is_connected()

    @classmethod
    def fazer_backup(cls, local_de_salvamento: Path):
        """Faz backup da base de dados"""

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
            messagebox.showinfo("Backup Concluído", f"Backup realizado com sucesso em {caminho_completo}")
            
        except Exception as e:
            # Exibe uma mensagem de erro
            messagebox.showerror("Erro ao fazer backup", f"Erro durante o backup: {e}")

        finally:
            # Remove o arquivo de opções após o uso
            arquivo_opcoes.unlink()

