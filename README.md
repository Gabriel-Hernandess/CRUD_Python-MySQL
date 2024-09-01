# Sistema de Cadastro e Login com Verificação de E-mail e CPF

## Descrição

Este é um sistema web simples desenvolvido em Python utilizando o Flask, que permite aos usuários se registrarem e efetuarem login. O sistema inclui funcionalidades para verificação de e-mail e CPF, garantindo a autenticidade dos dados fornecidos pelos usuários.

## Funcionalidades

- **Cadastro de Usuário:**
  - Verificação de e-mail utilizando uma expressão regular para garantir que o formato do e-mail seja válido.
  - Verificação de CPF utilizando a biblioteca `validate_docbr` para validar o CPF informado pelo usuário.
  - Envio de um código de verificação por e-mail para garantir que o endereço de e-mail fornecido seja válido.

- **Login de Usuário:**
  - Verificação do e-mail e senha para autenticar o usuário no sistema.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do sistema.
- **Flask**: Framework web utilizado para criar as rotas e a lógica do servidor.
- **MySQL**: Banco de dados utilizado para armazenar as informações dos usuários.
- **smtplib**: Biblioteca utilizada para enviar e-mails de verificação.
- **validate_docbr**: Biblioteca utilizada para validar o CPF dos usuários.
- **Flask-Mail**: Extensão do Flask utilizada para facilitar o envio de e-mails.

## Estrutura do Projeto

- **Cadastro:**
  - Verifica o formato do e-mail.
  - Verifica a existência do e-mail no banco de dados.
  - (Comentado) Verifica a validade do CPF.
  - Envia um código de verificação para o e-mail do usuário.
  - Após a verificação do código, registra o usuário no banco de dados.

- **Login:**
  - Verifica se o e-mail e a senha fornecidos correspondem a um usuário registrado no banco de dados.
  - Retorna uma mensagem de sucesso ou erro dependendo da validação.

## Configuração do Banco de Dados

O sistema utiliza um banco de dados MySQL. A estrutura do banco deve incluir uma tabela `usuarios` com as colunas `nome`, `email`, `senha`, e `cpf`.

## Autor

Desenvolvido por **Gabriel Hernandes**.

- **LinkedIn**: [Gabriel Hernandes]([https://br.linkedin.com/in/gabriel-hernandes-4a3b8b248?trk=people-guest_people_search-card](https://www.linkedin.com/in/gabriel-hernandess/))
- **GitHub**: [Gabriel-Hernandess](https://github.com/Gabriel-Hernandess)

## Considerações Finais

Este projeto é um exemplo básico de um sistema de autenticação que pode ser expandido com mais funcionalidades, como criptografia de senha, recuperação de conta, entre outras. Sugestões e colaborações são bem-vindas!
