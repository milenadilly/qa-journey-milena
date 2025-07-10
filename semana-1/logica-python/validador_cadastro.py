print("Validador de Cadastro de Usuário")  # Mensagem inicial

# Entrada de dados do usuário
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Digite uma senha: ")

erros = []  # Lista para guardar mensagens de erro

# Verifica se o nome está vazio
if nome.strip() == "":
    erros.append("O nome não pode estar em branco.")

# Verifica se o email tem "@" e "." (forma simples de validação)
if "@" not in email or "." not in email:
    erros.append("O email deve ser válido.")

# Verifica se a senha tem ao menos 6 caracteres
if len(senha) < 6:
    erros.append("A senha deve ter no mínimo 6 caracteres.")

# Se houver erros, mostra todos eles
if erros:
    print("Cadastro inválido:")
    for erro in erros:
        print(f"- {erro}")
else:
    print("Cadastro válido! Usuário criado com sucesso.")
