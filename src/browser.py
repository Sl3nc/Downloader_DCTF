from webbrowser import open, get, open_new_tab, open_new, Chrome
from pyautogui import (
    hotkey, moveTo, displayMousePosition, scroll, click, typewrite, press
)
from time import sleep

class Browser:
    """
    Classe responsável por automatizar o acesso ao sistema Acessorias.com para buscar e-mails de contato das empresas.
    """
    DOWNLOAD_URL = 'chrome://settings/downloads'
    ECAC_URL = 'https://cav.receita.fazenda.gov.br/autenticacao'

    def __init__(self, path: str):
        self.chrome_config(path)

    def chrome_config(self, path: str):
        open('https://www.google.com/')
        sleep(1)
        click(575, 63)
        typewrite(self.DOWNLOAD_URL)
        press('enter')
        sleep(2)

        # displayMousePosition()
        click(998, 235)
        sleep(1)
        typewrite(path.replace('/','\\'))
        sleep(1)
        press('tab')
        press('enter')

    def ecac(self):
        open_new_tab(self.ECAC_URL)

    def download_files(self):
        hotkey('alt', 'tab')
        self._filters()
        self._download()
        sleep(2)

    def _filters(self):
        scroll(100)

        #Período
        moveTo(47, 469)
        hotkey('ctrl', 'a')
        sleep(2)

        #Categoria
        moveTo(779, 449)
        sleep(2)
        
        #Procurador
        moveTo(26, 391)
        sleep(5)

        #Recibo
        moveTo(1264, 700)

    def _download(self):...

    def close(self):
        """
        Fecha a aba do ECAC.
        """
        hotkey('ctrl', 'w')

    def is_alive(self): 
        # get()
        ...