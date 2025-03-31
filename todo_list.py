# Sistema de Lista de Tarefas - Programação Funcional

tarefas = []

# Função de alta ordem
def aplicar_em_tarefas(func):
    return [func(tarefa) for tarefa in tarefas]

# Closure para adicionar tarefas
def criar_adicionador():
    def adicionar(nome=None, descricao=None):
        if not nome:
            nome = input("Digite o nome da tarefa: ").strip()
        if not descricao:
            descricao = input("Digite a descrição da tarefa: ").strip()
        tarefas.append({
            'nome': nome,
            'descricao': descricao,
            'concluida': False
        })
        print(f"Tarefa '{nome}' adicionada com sucesso!")
    return adicionar

adicionar_tarefa = criar_adicionador()

# Lambda para marcar tarefa como concluída
marcar_concluida = lambda indice: tarefas[indice].update({'concluida': True})

# Função com list comprehension para listar
def listar_tarefas():
    print("\n📋 Lista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        [print(f"{i+1}. {t['nome']} - {t['descricao']} - "
               f"{'✅ Concluída' if t['concluida'] else '⌛ Pendente'}")
         for i, t in enumerate(tarefas)]

# Função principal com menu
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Mostrar descrições das tarefas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a concluir: ")) - 1
                if 0 <= indice < len(tarefas):
                    marcar_concluida(indice)
                    print("Tarefa marcada como concluída.")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif opcao == '4':
            descricoes = aplicar_em_tarefas(lambda t: t['descricao'])
            print("📝 Descrições:", descricoes)
        elif opcao == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
