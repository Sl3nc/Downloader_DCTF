from kivy.uix.actionbar import BoxLayout
from kivy.lang import Builder
from kivy.app import App

Builder.load_file('window.kv')

class Step:
    value = 0
    message_index = 0
    func_index = 1
    browser = ...
    instructions = [
        ['Primeiramente, clique em "iniciar"', None],
        #Abre o navegador no passo 1
        ['Um navegador foi aberto na página do ECAC, certo?\nFaça login na conta da Deltaprice (clique em prosseguir quando acabar)', None]
    ]

    def __init__(self):
        pass

    def next(self) -> str:
        self.value = self.value + 1
        if self.value == len(self.instructions): self.value = 0
        data = self.instructions[self.value]

        func  = data[self.func_index]
        if func != None: func()

        return data[self.message_index]

    def back(self) -> str:
        self.value = self.value - 1
        return self.instructions[self.value][self.message_index]

    def jump(self) -> str:
        self.value = len(self.instructions) - 1
        return self.instructions[self.value][self.message_index]

class Downloader(BoxLayout):
    step = Step()
    pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ref = {
            0: lambda: self.step.next(),
            1: lambda: self.step.back(),
            2: lambda: self.step.jump()
        }

    #Executado pelo enviar / prosseguir
    def send(self, value = 0):
        result = self.ref[value]
        print(result())
        
        #Receber texto do botão também
        #Define o result como valor da instrunção


class DownloaderApp(App):
    def build(self):
        return Downloader()

if __name__ == '__main__':
    DownloaderApp().run()