from kivy.uix.rst import nodeclass
from kivy.uix.actionbar import Button
from kivy.uix.vkeyboard import Canvas
from kivy.uix.gesturesurface import Line
from kivy.uix.actionbar import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import BoxLayout
from kivy.app import App
from kivy.uix.widget import  Widget
from kivy.lang import Builder

Builder.load_file('window.kv')

class Downloader(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = 'vertical'

    #     self.add_widget(Label(
    #         text='Para baixar automaticamente seus recibos da DCTF WEB;\n'\
    #         'Siga as seguintes instrunções:',
    #         valign='top',
    #         halign='center'
    #     ))

    #     btns_box = BoxLayout(padding=20)
    #     btns_box.add_widget(Button(text='Enviar'))

    #     btns_utils_box = BoxLayout(orientation='vertical')
    #     btns_utils_box.add_widget(Button(text='Voltar'))
    #     btns_utils_box.add_widget(Button(text='Pular'))

    #     btns_box.add_widget(btns_utils_box)
    #     self.add_widget(btns_box)

class DownloaderApp(App):
    def build(self):
        return Downloader()

if __name__ == '__main__':
    DownloaderApp().run()