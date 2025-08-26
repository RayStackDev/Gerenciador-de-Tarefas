tarefas = []

def adicionar_tarefa():
    descricao = input("Digite a descriçao da tarefa: ").strip()
    if not descricao:
        print("Descriçao vazia nao é permitida.")
        return
    tarefas.append({'descriçao': descricao, 'concluida': False})
    print(f"Tarefa adicionada: {descricao}")

def listar_tarefas():
    if not tarefas:
        print("Sua lista está vazia.")
        return
    print("\nTarefas:")

    for i, t in enumerate(tarefas, start=1):
        status = "Feita" if t['concluida'] else "Esperando"
        print(f"{i}. {status} {t['descricao']}")

def escolher_indice(prompt):
    if not tarefas:
        print("Sua lista está vazia.")
        return None
    listar_tarefas()

    try:
        idx = int(input(prompt))
        if 1 <= idx <= len(tarefas):
            return idx - 1
        print("Numero fora do intervalo.")
        return None
    
    except ValueError:
        print("Digite um numero valido.")
        return None
    
def concluir_tarefa():
    i = escolher_indice("Numero da tarefa a concluir: ")
    if i is None:
        return
    tarefas[i]['concluida'] = True
    print(f"Conluida: {tarefas[i]['descricao']}")

def remover_tarefa():
    i = escolher_indice("Numero da tarefa a remover: ")
    if i is None:
        return
    removida = tarefas.pop(i)
    print(f"Removida: {removida['descricao']}")


while True:
    print("\n=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("5 - Sair\n")

    opcao = int(input("Escolha uma opçao: "))

    if opcao == 1:
        print("\nVocê escolheu adicionar uma tarefa.\n")
        adicionar_tarefa()
    elif opcao == 2:
        print("\nVocê escolheu listar uma tarefa.\n")
        listar_tarefas()
    elif opcao == 3:
        print("\nVocê escolheu concluir uma tarefa.\n")
        escolher_indice()
    elif opcao == 4:
        print("\nVocê escolheu remover uma tarefa.\n")
        remover_tarefa()
    elif opcao == 5:
        print("\nSaindo do programa.")
        break
    else:
        print("Opção Inválida, tente novamente")