# Criando uma lista vazia para o carrinho de compras
carrinho_de_compras = []

# Função para adicionar um item ao carrinho de compras
def adicionar_item():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade desejada: "))
    item = {"nome": nome, "preco": preco, "quantidade": quantidade}
    carrinho_de_compras.append(item)
    print(f"{quantidade} {nome}(s) adicionado(s) ao carrinho.")

# Função para excluir um item do carrinho de compras
def excluir_item():
    excluir_nome = input("Digite o nome do produto que deseja excluir: ")
    for item in carrinho_de_compras:
        if item["nome"] == excluir_nome:
            carrinho_de_compras.remove(item)
            print(f"{item['quantidade']} {item['nome']}(s) removido(s) do carrinho.")
            return
    print(f"{excluir_nome} não encontrado no carrinho.")

# Função para calcular o total da compra
def calcular_total():
    total = 0
    for item in carrinho_de_compras:
        total += item["preco"] * item["quantidade"]
    return total

# Função para exibir o recibo da compra
def exibir_recibo():
    print("Recibo de Compra:")
    for item in carrinho_de_compras:
        print(f"{item['quantidade']} {item['nome']}: R${item['preco'] * item['quantidade']:.2f}")
    print(f"Total: R${calcular_total():.2f}")

# Loop principal do programa
while True:
    print("\nOpções:")
    print("1. Adicionar item ao carrinho")
    print("2. Excluir item do carrinho")
    print("3. Exibir recibo da compra")
    print("4. Sair do programa")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        excluir_item()
    elif opcao == "3":
        exibir_recibo()
    elif opcao == "4":
        print("Obrigado por comprar conosco. Volte sempre!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
