from listar_itens import listar_itens

def marcar_como_comprado(lista_compras: list) -> None:
    listar_itens(lista_compras)
    indice = int(input("Digite o índice do item a ser marcado como comprado: ")) - 1
    if 0 <= indice < len(lista_compras):
        lista_compras[indice]["comprado"] = True
        print(f"Item '{lista_compras[indice]['nome']}' marcado como comprado!")
    else:
        print("Índice inválido.")
