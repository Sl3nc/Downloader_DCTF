from webbrowser import open
from time import sleep

class ECAC:
    """
    Classe responsável por automatizar o acesso ao sistema Acessorias.com para buscar e-mails de contato das empresas.
    """
    ROOT_URL = 'https://cav.receita.fazenda.gov.br/autenticacao/login'

    def __init__(self):
        open(self.ROOT_URL)

    def download_files(self):
        print('Entrou no Download')
        sleep(2)
    
    def close(self):
        """
        Fecha o navegador automatizado.
        """
        ...
        # self.browser.close()

    def is_alive(self): 
        ...