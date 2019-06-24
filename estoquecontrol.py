pro = [("789", "4009")]
produtos = dict(pro)
produtos.pop("789")
print()
print()
print()
print("Cadastro de Produtos")
print()
print()
print("[1] Cadastrar Produtos")
print("[2] Consultar Produtos")
print("[3] Sair")
print()
print()

op1 = int(input("Opção Desejada"))

while op1 !=3:

    if op1 == 1:
        insert = input("Código")
        produtos[insert] = float(input("Valor"))

    elif op1 == 2:
        print(produtos)
    
