from flask import Flask, request, abort, redirect
import mysql.connector
import re
from validate_docbr import CPF
import smtplib
import email.message
from random import randint
from flask_mail import Mail, Message

global db

# coloque seu banco de dados
conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database=''
)

register_connection = Flask(__name__)

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao, email)


def verificar_cpf(cpf):
    cpf_sem_formato = cpf
    cpf_com_formato = cpf_sem_formato.replace(".", "").replace("-", "")
    cpf_validator = CPF()
    
    if cpf_validator.validate(cpf_com_formato):
        cpf_verify = True
        print("CPF válido")
    else:
        cpf_verify = False
        print("CPF inválido")
        
    return cpf_verify

def enviar_email():  
    codigo = randint(0, 999999)

    global db
    db = codigo
    
    corpo_email = f"Bem Vindo ao site oficial do Teatro de Ourinhos. Seu codigo de verificacao e: {codigo}"

    msg = email.message.Message()
    msg['Subject'] = "Codigo de Verificacao"
    msg['From'] = '' # seu email, ao qual ira mandar o codigo para o usuario
    msg['To'] = request.form['email_register']
    password = '' # sua senha do google para fins de testes, leia mais sobre isso na net
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    print('Email enviado')


@register_connection.route("/register_db", methods=['POST'])

def register_db():
    global Email, senha, nome, cpf
    Email = request.form['email_register']
    senha = request.form['senha_register']
    nome = request.form['nome_register']
    cpf = request.form['cpf_register']
    
    if not validar_email(Email):
        abort(400, 'E-mail inválido')


    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (Email,))
    todos_usuarios = cursor.fetchall()
    
    if len(todos_usuarios) > 0:
        cursor.close()
        abort(400, 'Email ja cadastrado!')
    cursor.close()

    #if not verificar_cpf(cpf):
       # abort(400, 'CPF inválido') 
    
    enviar_email()

    return redirect('../Cadastro/verificar.html')

@register_connection.route("/verificar", methods=['POST'])

def Verificar():
    global email, senha, nome, cpf, db
    user_code = request.form['code']

    if int(db) == int(user_code):
        cursor = conexao.cursor()
        cursor.execute(f'INSERT INTO usuarios (nome, email, senha, cpf) VALUES ("{nome}", "{Email}", "{senha}", "{cpf}")')
        conexao.commit()

        cursor.close()
        conexao.close()

        return "registrado com sucesso"

    else:
        abort(400, 'Nao foi possivel verificar, tente novamente')
    

if __name__ == '__main__':
    register_connection.run()