import NodeState

class EightPuzz:
    def __init__(self, initial_state):
        # inicializa o estado inicial do quebra-cabeça e o estado objetivo
        self.initial_state = NodeState(initial_state)  # cria uma nova instância de NodeState com o estado inicial
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # define o estado objetivo do quebra-cabeça
        self.max_depth = 20  # define o limite de profundidade para a busca iterativa em profundidade (iddfs)

    def is_goal_state(self, state):
        # verifica se o estado atual é o estado objetivo
        return state.board == self.goal_state

    def dls(self, state, depth, path):
        # realiza a busca em profundidade limitada
        if self.is_goal_state(state):
            # se o estado atual for o estado objetivo, retorna o caminho até aqui
            return path + [state.board]

        if depth == 0:
            # se a profundidade máxima for alcançada, retorna None
            return None

        for move in state.get_possible_moves():
            # itera sobre os movimentos possíveis
            new_state = NodeState(state.board)  # cria uma nova cópia do estado atual
            new_state.make_move(move)  # aplica o movimento ao novo estado
            new_state.print_board()  # mostra o novo estado do tabuleiro

            result = self.dls(new_state, depth - 1, path + [state.board])  # chama recursivamente a dls com o novo estado
            if result:
                return result  # retorna o resultado se encontrado

        return None  # retorna None se nenhum resultado for encontrado

    def solve(self):
        # resolve o quebra-cabeça tentando diferentes profundidades
        for depth in range(self.max_depth + 1):
            result = self.dls(self.initial_state, depth, [])  # inicia a busca a partir do estado inicial
            if result:
                print("solução encontrada:")
                for step in result:
                    print(step)  # imprime cada passo da solução
                return result  # retorna a solução encontrada

        print("nenhuma solução encontrada.")  # mensagem se não houver solução
        return None

    def get_inv_count(self):
        # conta o número de inversões no estado inicial
        flat_state = [j for sub in self.initial_state.board for j in sub]  # transforma o tabuleiro em uma lista linear
        inversions = 0  # inicializa o contador de inversões
        for i in range(0, 9):
            for j in range(i + 1, 9):
                # conta quantas inversões existem
                if flat_state[j] != 0 and flat_state[i] != 0 and flat_state[i] > flat_state[j]:
                    inversions += 1
        return inversions  # retorna o número total de inversões

    def is_solvable(self):
        # verifica se o quebra-cabeça pode ser resolvido
        return self.get_inv_count() % 2 == 0  # um quebra-cabeça é solucionável se o número de inversões for par
