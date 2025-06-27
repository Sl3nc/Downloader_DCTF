from pathlib import Path
from json import load

class Step:
    """
    Classe responsável por gerenciar as etapas (steps) do fluxo de instruções da aplicação.

    Permite avançar, retroceder, pular etapas e identificar quando é o momento de execução automática.
    """
    value = -1
    max_value = -1
    min_value = -1
    message_index = 'message'
    func_index = 'func'
    label_index = 'label'
    instruction_path = Path(__file__).parent / 'json' / 'instructions.json'
    instructions = ''

    def __init__(self):
        """
        Inicializa a classe Step, carregando as instruções do arquivo JSON.
        """
        self.utils_ref = {
            0: lambda: True,
            1: lambda: self.value < self.max_value
        }

        with open(self.instruction_path, 'r', encoding='utf-8') as file:
            self.instructions = load(file)
        pass

    def next(self) -> str:
        """
        Avança para a próxima etapa e retorna o label e mensagem correspondentes.
        """
        if self.value != len(self.instructions) - 1: self.value = self.value + 1
        return self._data(self.value)

    def back(self) -> str:
        """
        Retorna para a etapa anterior, atualizando o valor máximo alcançado.
        """
        if self.max_value < self.value \
            and self.value < len(self.instructions) - 1:
            self.max_value = self.value
        if self.value != 0: self.value = self.value - 1

        return self._data(self.value)

    def jump(self) -> str:
        """
        Pula para a próxima etapa que exige execução automática.
        """
        for i in range(self.value + 1, len(self.instructions)):
            if self.instructions[i][self.func_index]:
                self.value = i
                return self._data(i)

        return self._data(self.value)
    
    def is_execution_time(self):
        """
        Verifica se a etapa atual exige execução automática.
        """
        func  = self.instructions[self.value][self.func_index]
        return True if func == True and self.value >= self.max_value else False

    def _data(self, value):
        """
        Retorna o label e mensagem da etapa especificada.
        """
        data = self.instructions[value]
        return data[self.label_index], data[self.message_index]
    
    def start(self):
        """
        Reinicia o controle de etapas para o início do fluxo.
        """
        self.value = self.min_value
        self.max_value = self.min_value