from webbrowser import open, get, open_new_tab, open_new, Chrome
from pyautogui import (
    hotkey, displayMousePosition, scroll, click, typewrite, press,
    locateAllOnScreen, locateOnScreen, useImageNotFoundException,
    size
)
from time import sleep
from pathlib import Path
from pygetwindow import getWindowsWithTitle

class Browser:
    """
    Classe responsável por automatizar o acesso ao sistema Acessorias.com para buscar e-mails de contato das empresas.
    """
    DOWNLOAD_URL = 'chrome://settings/downloads'
    ECAC_URL = 'https://cav.receita.fazenda.gov.br/autenticacao'
    next_arrow_path = (Path(__file__).parent / 'imgs' / 'next_arrow.png').__str__()
    recibo_path = (Path(__file__).parent / 'imgs' / 'recibo.png').__str__()

    def __init__(self, path: str):
        useImageNotFoundException(False)
        self.chrome_config(path)
        pass

    def chrome_config(self, path: str):
        open('https://www.google.com/')
        sleep(1)

        self.reposite_window()
        
        self.__enter_config()

        # displayMousePosition()
        click(400, 250, 3)
        hotkey('ctrl', 'c')

        self.__entry_download_path(lambda: typewrite(path.replace('/','\\')))

    def reposite_window(self):
        chrome = getWindowsWithTitle('Google - Google Chrome')[0]
        window_x = chrome.left + 8
        screen_x = size()[0]

        if screen_x <= window_x : chrome.moveTo(-8, -8)
        if chrome.isMaximized == False: chrome.maximize()

    def chrome_reset(self):
        self.__enter_config()
        self.__entry_download_path(lambda: hotkey('ctrl', 'v'))

    def __entry_download_path(self, func):
        click(998, 235)
        sleep(1)
        func()
        sleep(1)
        press('tab')
        press('enter')

    def __enter_config(self):
        click(575, 63)
        typewrite(self.DOWNLOAD_URL)
        press('enter')
        sleep(2)

    def ecac(self):
        open_new_tab(self.ECAC_URL)

    def download_files(self, start_date: str, end_date: str):
        hotkey('alt', 'tab')
        self._filters(start_date, end_date)
        self._download()
        sleep(2)

    def _filters(self, start_date: str, end_date: str):
        ref = {
            47: lambda: typewrite(start_date),
            157: lambda: typewrite(end_date),
            385: lambda: press('backspace'),
            488: lambda: press('backspace')
        }
        scroll(1000)

        #Procurador
        click(26, 391)
        sleep(8)
        
        #Período
        for pos, entry in ref.items():
            click(pos, 484, 4)
            entry()
            press('enter')
        
        #Categoria
        click(779, 459)
        click(742, 502)

        #Botão de pesquisa
        click(582, 579)
        sleep(3)

    def _download(self):
        arrow_pos = 0

        while arrow_pos != None :
            scroll(-500)
            sleep(0.5)

            #Recibo
            for i in locateAllOnScreen(self.recibo_path):
                click(i)
                sleep(2.5)
                click(i)
                sleep(0.5)

            scroll(-500)
            sleep(0.5)
            scroll(-500)
            sleep(0.5)

            arrow_pos = locateOnScreen(self.next_arrow_path)
            if arrow_pos != None:
                click(arrow_pos)
                sleep(3)
        
    def close(self):
        """
        Fecha a aba do ECAC.
        """
        hotkey('ctrl', 'w')

    def is_alive(self): 
        # get()
        ...