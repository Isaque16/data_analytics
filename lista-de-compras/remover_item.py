from listar_itens import listar_itens

def remover_item(lista_compras: list) -> None:
    listar_itens(lista_compras)
    indice = int(input("Digite o índice do item a ser removido: ")) - 1
    if 0 <= indice < len(lista_compras):
        item_removido = lista_compras.pop(indice)
        print(f"Item '{item_removido['nome']}' removido com sucesso!")
    else:
        print("Índice inválido.")
