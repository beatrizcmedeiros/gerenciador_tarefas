def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada" : False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas: ")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1

    if(indice_tarefa_ajustado  >= 0 and indice_tarefa_ajustado < len(tarefas)):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"\nTarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("\nÍndice de tarefa inválido.")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1

    if(indice_tarefa_ajustado  >= 0 and indice_tarefa_ajustado < len(tarefas)):
        tarefas[indice_tarefa_ajustado]["completada"] = True
        print(f"\nTarefa {indice_tarefa} marcada como completada.")
    else:
        print("\nÍndice de tarefa inválido.")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if(tarefa["completada"]):
            tarefas.remove(tarefa)
    print("As tarefas completadas foram deletadas.")
    return

tarefas = []

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair\n")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("\nDigite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("\nDigite o número da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("\nDigite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        confirmar_decisao = input("\nTem cereteza que deseja deletar as tarefas completadas? (S/N) ")
        if confirmar_decisao == "S":
            deletar_tarefas_completadas(tarefas)
            ver_tarefas(tarefas)
        elif confirmar_decisao == "N":   
            print("\nNenhuma tarefa foi deletada.")
        else:
            print("\nComando inválido. Nenhuma tarefa foi deletada.")
    elif escolha == "6":
        break

print("\nPrograma finalizado.\n")