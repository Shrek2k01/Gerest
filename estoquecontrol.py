pro = [("789", "4009")]
produtos = dict(pro)
produtos.pop("789")
op1=0
while op1 !=3:
    print("\n"*500)
    print("Cadastro de Produtos")
    print("[1] Cadastrar Produtos")
    print("[2] Consultar Produtos")
    print("[3] Sair")
    p1 = int(input("Opção Desejada"))
    if op1 ==1:
        opcao = 0
        while opcao !=2:
            print("\n"*500)
            insert = input("Código")
            produtos[insert] = float(input("Valor"))
            print("\n"*500)
            print("[1] Continuar a cadastrar")
            print("[2] Sair e Salvar")
            print()
            opcao = int(input("Opção:"))
            print("\n"*500)
    elif op1 == 2:
        print("\n"*500)
        print(produtos)
        opcao02 = input("Enter para Sair")

    
