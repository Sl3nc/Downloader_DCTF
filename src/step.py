class Step:
    value = 0
    max_value = 0
    message_index = 'message'
    func_index = 'func'
    label_index = 'label'
    browser = ...
    instructions = [
        {
            'message': 'Primeiramente, clique em "iniciar"', 
            'label': 'Iniciar',
            'func': None
        },
        {
            'message': 'Um navegador foi aberto na página do ECAC, certo?\nFaça login na conta da Deltaprice (clique em prosseguir quando acabar)', 
            'label': 'Prosseguir',
            #Abre o navegador no passo 1
            'func': lambda: print('\noi')
        },
        {
            'message': 'Agora faça o seguinte', 
            'label': 'Executar',
            'func': None
        }
    ]

    def __init__(self):
        pass

    def next(self) -> str:
        if self.value != len(self.instructions) - 1: self.value = self.value + 1

        func  = self.instructions[self.value][self.func_index]
        if func != None and self.value > self.max_value: func()

        return self._data(self.value)

    def back(self) -> str:
        if self.value != 0: self.value = self.value - 1
        if self.max_value < self.value: self.max_value = self.value

        return self._data(self.value)

    def jump(self) -> str:
        self.value = len(self.instructions) - 1
        return self._data(self.value)

    def _data(self, value):
        data = self.instructions[value]
        return data[self.label_index], data[self.message_index]
    
    def __call__(self, *args, **kwds):
        return self._data(0)