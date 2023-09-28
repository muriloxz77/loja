import os
from classes import *

cliente = Cliente()
loja = Produtos()
adm = Adm()  # O administrador padrão é - Nome: admin - Senha: admin

def menu_login(cliente, loja, adm):
    while True:
        print("\n==== MENU DE LOGIN ====")
        print("1. Login como Cliente")
        print("2. Login como Administrador")
        print("3. Sair")
        menu = input("Escolha uma opção: ")

        if menu == "1":
            nome = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            if cliente.logar_cliente(nome, senha):
                print("Login bem-sucedido como cliente.")
                menu_cliente(cliente, loja)
            else:
                print("Nome de usuário ou senha incorretos.")
        elif menu == "2":
            nome = input("Digite o nome de administrador: ")
            senha = input("Digite a senha de administrador: ")
            if adm.verificar_adm(nome, senha):
                print("Login bem-sucedido como administrador.")
                menu_adm(adm, cliente, loja)
            else:
                print("Nome de administrador ou senha incorretos.")
        elif menu == "3":
            print("Saindo...")
            os.system("pause")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_cliente(cliente, loja):
    while True:
        print("\n==== MENU CLIENTE ====")
        print("1. Adicionar produto no carrinho")
        print("2. Excluir produto do carrinho")
        print("3. Listar produtos no carrinho")
        print("4. Comprar")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            loja.listar_produtos_loja()
            indice = int(input("Digite o índice do produto que deseja adicionar ao carrinho: "))
            indice += 1
            loja.add_produto_carrinho(indice)
        elif escolha == "2":
            loja.listar_produtos_carrinho()
            indice = int(input("Digite o índice do produto que deseja excluir do carrinho: "))
            loja.del_produto_carrinho(indice)
        elif escolha == "3":
            loja.listar_produtos_carrinho()
        elif escolha == "4":
            loja.realizar_compra(cliente)
        elif escolha == "5":
            print("Saindo...")
            os.system("pause")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_adm(adm, cliente, loja):
    while True:
        print("\n==== MENU ADM ====")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Adm")
        print("3. Cadastrar Produto na Loja")
        print("4. Excluir Produto da Loja")
        print("5. Listar Produtos na Loja")
        print("6. Listar Clientes")
        print("7. Gerar Relatório de Vendas")
        print("8. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do novo cliente: ")
            senha = input("Digite a senha do novo cliente: ")
            cliente.adicionar_cliente(nome, senha)
            print("Cliente cadastrado com sucesso.")
            os.system("pause")
        elif escolha == "2":
            nome = input("Digite o nome do novo administrador: ")
            senha = input("Digite a senha do novo administrador: ")
            adm.cadastrar_adm(nome, senha)
            print("Administrador cadastrado com sucesso.")
        elif escolha == "3":
            nome = input("Nome do produto: ")
            valor = float(input("Valor do produto: "))
            produto = Produto(nome, valor)
            loja.inserir_produto_loja(produto)
            print("Produto adicionado com sucesso")
            os.system("pause")
        elif escolha == "4":
            loja.listar_produtos_loja()
            indice = int(input("Digite o índice do produto que deseja excluir: "))
            loja.del_produto_loja(indice)
            os.system("pause")
        elif escolha == "5":
            loja.listar_produtos_loja()
            os.system("pause")
        elif escolha == "6":
            cliente.listar_clientes()
            os.system("pause")
        elif escolha == "7":
            loja.gerar_relatorio_vendas()
            os.system("pause")
        elif escolha == "8":
            print("Saindo...")
            os.system("pause")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Login")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_login(cliente, loja, adm)
        elif escolha == "2":
            print("Saindo...")
            os.system("pause")
            break
        else:
            print("Opção inválida. Tente novamente.")