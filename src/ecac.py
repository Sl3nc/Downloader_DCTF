from selenium.common.exceptions import (
    NoSuchElementException, SessionNotCreatedException
)
from selenium.webdriver.chrome.service import Service
from driver_maintenanse import DriverMaintenance
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
from time import sleep

class ECAC:
    """
    Classe responsável por automatizar o acesso ao sistema Acessorias.com para buscar e-mails de contato das empresas.
    """
    ROOT_FOLDER = Path(__file__).parent
    CHROME_DRIVER_PATH = ROOT_FOLDER / 'driver' / 'chromedriver.exe'
    ROOT_URL = 'https://cav.receita.fazenda.gov.br/autenticacao/login'
    URL_DETALHES = 'https://app.acessorias.com/sysmain.php?m=105&act=e&i={0}&uP=14&o=EmpNome,EmpID|Asc'

    INPUT_EMAIL = 'mailAC'
    INPUT_PASSWORD= 'passAC'
    BTN_ENTRAR = '#site-corpo > section.secao.secao-login > div > form > div.botoes > button'

    def __init__(self):
        self.browser = self.make_chrome_browser()
        self.browser.get(self.ROOT_URL)

    def make_chrome_browser(self,*options: str) -> webdriver.Chrome:
        """
        Cria uma instância do navegador Chrome para automação.
        """
        try:
            chrome_options = webdriver.ChromeOptions()

            if options is not None:
                for option in options:
                    chrome_options.add_argument(option)

            chrome_service = Service(
                executable_path=str(self.CHROME_DRIVER_PATH),
            )

            browser = webdriver.Chrome(
                service=chrome_service,
                options=chrome_options
            )

            return browser
        except SessionNotCreatedException:
            DriverMaintenance().upgrade()
            return self.make_chrome_browser()
        
    def hide(self):
        self.browser.set_window_position(-10000,0)

    def download_files(self):
        print('Entrou no Download')
        sleep(2)
    
    def close(self):
        """
        Fecha o navegador automatizado.
        """
        self.browser.close()

    def is_alive(self): self.browser.current_url