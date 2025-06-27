from webbrowser import open, get, open_new_tab, open_new, Chrome, register, BackgroundBrowser
from pyautogui import (
    hotkey, moveTo, displayMousePosition, scroll, click, typewrite, press,
    locateAllOnScreen, locateOnScreen, dragTo, useImageNotFoundException,
    size, onScreen
)
from time import sleep
from pathlib import Path
from tkinter.filedialog import askdirectory
from traceback import print_exc
from screen import Screen

class Browser:
    """
    Classe responsável por automatizar o acesso ao sistema Acessorias.com para buscar e-mails de contato das empresas.
    """
    DOWNLOAD_URL = 'chrome://settings/downloads'
    ECAC_URL = 'https://cav.receita.fazenda.gov.br/autenticacao'
    enterprise_control_path = (
        Path(__file__).parent / 'imgs' / 'interprise_control_chrome.png'
    ).__str__()
    next_arrow_path = (Path(__file__).parent / 'imgs' / 'next_arrow.png').__str__()
    recibo_path = (Path(__file__).parent / 'imgs' / 'recibo.png').__str__()
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    can_execute = True
    
    current_download_pos = [400, 250]
    change_download_pos = [998, 235]
    extra_download_y = 40

    def __init__(self, path: str):
        self.screen = Screen()
        self.extra_download = [
            self.current_download_pos,
            self.change_download_pos
        ]

        register('chrome', None, BackgroundBrowser(self.chrome_path))
        self.controller = get('chrome')
        useImageNotFoundException(False)
        self.chrome_config(path)
        pass

    def chrome_config(self, path: str):
        self.controller.open('https://www.google.com/')
        sleep(2)

        self.screen.reposite('Google - Google Chrome')

        self.__enter_url(self.DOWNLOAD_URL)

        if locateOnScreen(self.enterprise_control_path) != None:
            for i in self.extra_download:
                i[1] = i[1] + self.extra_download_y

        # displayMousePosition()
        click(*self.current_download_pos, 3)
        hotkey('ctrl', 'c')

        self.__entry_download_path(lambda: typewrite(path.replace('/','\\'))) 

    def chrome_reset(self):
        hotkey('ctrl', 'w')
        self.__entry_download_path(lambda: hotkey('ctrl', 'v'))

    def __entry_download_path(self, func):
        click(self.change_download_pos)
        sleep(1)
        func()
        sleep(1)
        press('tab')
        press('enter')
        sleep(1)

    def ecac(self):
        self.controller.open_new_tab(self.ECAC_URL)
        
    def __enter_url(self, url):
        click(575, 63)
        typewrite(url)
        sleep(0.5)
        press('enter')
        sleep(2)

    def download_files(self, start_date: str, end_date: str):
        hotkey('alt', 'tab')
        self._filters(start_date, end_date)
        sleep(5)
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
        sleep(9)
        
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

    def _download(self):
        arrow_pos = 0

        while arrow_pos != None and self.can_execute:
            scroll(-500)
            sleep(1)

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
        # hotkey('ctrl', 'w')
        self.screen.reset()

    def is_alive(self): 
        # get()
        ...

    def cancel(self): self.can_execute = False