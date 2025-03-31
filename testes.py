from todo_list import criar_adicionador, listar_tarefas, marcar_concluida, aplicar_em_tarefas

adicionar = criar_adicionador()

print("\n==== CT01 - Adicionar Tarefas ====")
adicionar("Estudar Python", "Revisar programação funcional")
adicionar("Fazer exercícios", "Resolver lista de exercícios da disciplina")
adicionar("Enviar atividade", "Subir no GitHub e avisar a equipe")

print("\n==== CT02 - Listar Tarefas ====")
listar_tarefas()

print("\n==== CT03 - Marcar tarefa como concluída ====")
marcar_concluida(1)  # Marca a segunda como concluída

print("\n==== CT04 - Ver tarefas atualizadas ====")
listar_tarefas()

print("\n==== CT05 - Função de Alta Ordem ====")
descricoes = aplicar_em_tarefas(lambda t: t['descricao'])
print("Descrições das tarefas:", descricoes)
