while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair\n")

    opcao = int(input("Escolha uma opçao: "))

    if opcao == 1:
        print("\nVocê escolheu adicionar uma tarefa.")
    elif opcao == 2:
        print("\nVocê escolheu listar uma tarefa.")
    elif opcao == 3:
        print("\nVocê escolheu concluir uma tarefa.")
    elif opcao == 4:
        print("\nVocê escolheu remover uma tarefa.")
    elif opcao == 5:
        print("\nSaindo do programa.")
        break
    else:
        print("Opção Inválida, tente novamente")

tarefas = []

def adicionar_tarefa():
    descricao = input("Digite a descriçao da tarefa: ").strip()
    if not descricao:
        print("Descriçao vazia nao é permitida.")
        return
    tarefas.append({'descriçao': descricao, 'concluida': False})
    print(f"Tarefa adicionada: {descricao}")
