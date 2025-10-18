class Tarefa:
    def __init__(self, nome, descricao):
        if not nome:
            raise ValueError("O nome da tarefa não pode ser vazio.")
        self.nome = nome
        self.descricao = descricao
        self.status = "em andamento"

    def marcar_concluida(self):
        if self.status == "concluída":
            raise ValueError("A tarefa já está concluída.")
        self.status = "concluída"

    def marcar_em_andamento(self):
        if self.status == "concluída":
            raise ValueError("Não é possível marcar como 'em andamento' uma tarefa concluída.")
        self.status = "em andamento"

    def editar(self, novo_nome, nova_descricao):
        if not novo_nome:
            raise ValueError("O nome da tarefa não pode ser vazio.")
        self.nome = novo_nome
        self.descricao = nova_descricao


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome, descricao):
        tarefa = Tarefa(nome, descricao)
        self.tarefas.append(tarefa)
        return tarefa

    def encontrar_tarefa(self, nome):
        for tarefa in self.tarefas:
            if tarefa.nome == nome:
                return tarefa
        return None

    def excluir_tarefa(self, nome):
        tarefa = self.encontrar_tarefa(nome)
        if tarefa:
            self.tarefas.remove(tarefa)
        else:
            raise ValueError("Tarefa inexistente.")
