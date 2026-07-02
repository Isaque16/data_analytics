def listar_itens(lista_compras: list) -> None:
    if not lista_compras:
        print("A lista está vazia, adicione um novo item digitando 1.")
        return
    for item in lista_compras:
        status = "✓" if item["comprado"] else "✗"
        print(f"{status} {item['nome']} - {item['quantidade']}")
