from flask import Flask, request, abort
import mysql.connector

# coloque seu banco de dados
conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database=''
)

login_connection = Flask(__name__)

@login_connection.route("/login_db", methods=['POST'])

def login_db():
    email = request.form['email_login']
    senha = request.form['senha_login']
    
    # chama o comando sql para verificar se as variaveis puxadas do flask, email e senha, estao na tabela sql, se sim, efetua login, se nao, erro.
    cursor = conexao.cursor()
    cursor.execute(f'SELECT * FROM usuarios WHERE email = "{email}" AND senha = "{senha}"')
    
    # Use fetchall() para buscar todos os resultados da consulta
    results = cursor.fetchall()
    
    # Verifique se a consulta retornou algum resultado
    if len(results) > 0:
        print("A variável está cadastrada na tabela!")
        return "Login realizado com sucesso!"
    else:
        print("A variável não está cadastrada na tabela.")
        abort(401, 'Invalid email or password')

    cursor.close()
    conexao.close()

if __name__ == '__main__':
    login_connection.run()