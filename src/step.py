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
            'func': False
        },
        {
            'message': 'Insira a pasta onde será feito os downloads', 
            'label': 'Prosseguir',
            'func': True
        },
        {
            'message': 'Um navegador foi aberto na página do ECAC, certo?\nFaça login na conta da Deltaprice\n(clique em prosseguir quando acabar)', 
            'label': 'Prosseguir',
            'func': False
        },
        {
            'message': 'Tudo pronto!\nAgora que está na tela ideal, clique em "Executar"', 
            'label': 'Executar',
            'func': False
        },
        {
            'message': 'A janela foi minimizada e a operação está ocorrendo, acompanhe seu progresso na barra abaixo', 
            'label': 'Executar',
            'func': True
        },
    ]

    def __init__(self):
        pass

    def next(self) -> str:
        if self.value != len(self.instructions) - 1: self.value = self.value + 1
        return self._data(self.value)

    def back(self) -> str:
        if self.value != 0: self.value = self.value - 1
        if self.max_value < self.value: self.max_value = self.value

        return self._data(self.value)

    def jump(self) -> str:
        self.value = len(self.instructions) - 1
        return self._data(self.value)
    
    def is_execution_time(self):
        func  = self.instructions[self.value][self.func_index]
        return True if func == True and self.value > self.max_value else False

    def _data(self, value):
        data = self.instructions[value]
        return data[self.label_index], data[self.message_index]
    
    def __call__(self, *args, **kwds):
        return self._data(0)