from win32api import GetSystemMetrics, EnumDisplaySettings, ChangeDisplaySettings
from pygetwindow import getWindowsWithTitle
from time import sleep

class Screen:
    """
    Classe responsável por manipular a resolução da tela e posicionamento da janela do navegador.

    Permite alterar a resolução para garantir compatibilidade com a automação e restaurar ao final do processo.
    """
    width = 1366
    height = 768
    deft = 32
    was_changed = False

    def __init__(self):
        """
        Inicializa a classe obtendo a resolução atual da tela.
        """
        self.x =  GetSystemMetrics(0)
        self.y = GetSystemMetrics(1)
        pass

    def reposite(self, title: str):
        """
        Reposiciona e maximiza a janela do navegador, ajustando a resolução se necessário.
        """
        browser = getWindowsWithTitle(title)[0]
        window_x = browser.left + 8

        if self.x <= window_x : 
            browser.moveTo(-8, -8)
            sleep(1)

        if self.x != self.width : 
            mode = EnumDisplaySettings()
            mode.PelsWidth = self.width
            mode.PelsHeight = self.height
            mode.BitsPerPel = self.deft
            self.was_changed = True

            ChangeDisplaySettings(mode, 0)
            sleep(3)

        if browser.isMaximized == False: browser.maximize()

    def reset(self):
        """
        Restaura a resolução original da tela caso tenha sido alterada.
        """
        if self.was_changed:
            mode = EnumDisplaySettings()
            mode.PelsWidth = self.x
            mode.PelsHeight = self.y
            mode.BitsPerPel = self.deft
            ChangeDisplaySettings(mode, 0)
