import unittest
from atividade import ListaDeTarefas, Tarefa


class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.lista = ListaDeTarefas()

    # TEST-01
    def test_adicionar_tarefa_valida(self):
        tarefa = self.lista.adicionar_tarefa("Estudar", "Ler capítulo 3 de Python")
        self.assertEqual(tarefa.nome, "Estudar")
        self.assertEqual(tarefa.descricao, "Ler capítulo 3 de Python")
        self.assertIn(tarefa, self.lista.tarefas)

    # TEST-02
    def test_nao_permitir_tarefa_sem_nome(self):
        with self.assertRaises(ValueError):
            self.lista.adicionar_tarefa("", "Descrição qualquer")

    # TEST-03
    def test_marcar_tarefa_como_concluida(self):
        tarefa = self.lista.adicionar_tarefa("Estudar", "Ler capítulo 3")
        tarefa.marcar_concluida()
        self.assertEqual(tarefa.status, "concluída")

    # TEST-04
    def test_nao_pode_marcar_tarefa_concluida_novamente(self):
        tarefa = self.lista.adicionar_tarefa("Estudar", "Ler capítulo 3")
        tarefa.marcar_concluida()
        with self.assertRaises(ValueError):
            tarefa.marcar_concluida()

    # TEST-05
    def test_marcar_tarefa_em_andamento(self):
        tarefa = self.lista.adicionar_tarefa("Treinar", "Ir à academia")
        tarefa.marcar_em_andamento()
        self.assertEqual(tarefa.status, "em andamento")

    # TEST-06
    def test_nao_pode_marcar_em_andamento_se_concluida(self):
        tarefa = self.lista.adicionar_tarefa("Treinar", "Ir à academia")
        tarefa.marcar_concluida()
        with self.assertRaises(ValueError):
            tarefa.marcar_em_andamento()

    # TEST-07
    def test_editar_tarefa(self):
        tarefa = self.lista.adicionar_tarefa("Estudar", "Ler capítulo 3")
        tarefa.editar("Estudar Python", "Ler capítulo 4")
        self.assertEqual(tarefa.nome, "Estudar Python")
        self.assertEqual(tarefa.descricao, "Ler capítulo 4")

    # TEST-08
    def test_editar_tarefa_inexistente(self):
        tarefa = self.lista.encontrar_tarefa("Nada")
        self.assertIsNone(tarefa)

    # TEST-09
    def test_excluir_tarefa_existente(self):
        tarefa = self.lista.adicionar_tarefa("Estudar", "Ler capítulo 3")
        self.lista.excluir_tarefa("Estudar")
        self.assertNotIn(tarefa, self.lista.tarefas)

    # TEST-10
    def test_excluir_tarefa_inexistente(self):
        with self.assertRaises(ValueError):
            self.lista.excluir_tarefa("Inexistente")
