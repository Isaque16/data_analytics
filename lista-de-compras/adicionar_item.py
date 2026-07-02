def adicionar_item(lista_compras: list) -> None:
    while True:
        nome = input("Digite o nome do item: ")
        if not nome:
            print("Nome do item não pode ser vazio.")
            continue
        break
    while True:
        quantidade = input("Digite a quantidade: ")
        if not quantidade:
            print("Quantidade do item não pode ser vazia.")
            continue
        break
    item = {"nome": nome, "quantidade": quantidade, "comprado": False}
    lista_compras.append(item)
    print(f"Item '{nome}' adicionado com sucesso!")
