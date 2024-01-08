import mysql.connector as mysql

# Usa o padrão de projeto Singleton para a conexão do banco de dados
class Conexao:
    _conexao = None  # Atributo Protegido!!!

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
                database=db_name
            )
        except Exception as e:
            # Mostra uma mensagem de erro
            ...
            
    @classmethod
    def get_conexao(cls):
        if cls._conexao is None:
            raise Exception("A conexão não está configurada. Use o método 'configurar' primeiro.")
        return cls._conexao
    
    @classmethod
    def fechar_conexao(cls):
        if cls._conexao:
            cls._conexao.close()
            print("Conexão fechada.")

