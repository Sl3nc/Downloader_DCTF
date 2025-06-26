from pathlib import Path
from json import load

class Step:
    value = -1
    max_value = -1
    min_value = -1
    message_index = 'message'
    func_index = 'func'
    label_index = 'label'
    instruction_path = Path(__file__).parent / 'json' / 'instructions.json'
    instructions = ''

    def __init__(self):
        self.utils_ref = {
            0: lambda: True,
            1: lambda: self.value < self.max_value
        }

        with open(self.instruction_path, 'r', encoding='utf-8') as file:
            self.instructions = load(file)
        pass

    def next(self) -> str:
        if self.value != len(self.instructions) - 1: self.value = self.value + 1
        return self._data(self.value)

    def back(self) -> str:
        if self.max_value < self.value \
            and self.value < len(self.instructions) - 1:
            self.max_value = self.value
        if self.value != 0: self.value = self.value - 1

        return self._data(self.value)

    def jump(self) -> str:
        for i in range(self.value + 1, len(self.instructions)):
            if self.instructions[i][self.func_index]:
                self.value = i
                return self._data(i)

        return self._data(self.value)
    
    def is_execution_time(self):
        func  = self.instructions[self.value][self.func_index]
        return True if func == True and self.value >= self.max_value else False

    def _data(self, value):
        data = self.instructions[value]
        return data[self.label_index], data[self.message_index]
    
    def start(self):
        self.value = self.min_value
        self.max_value = self.min_value