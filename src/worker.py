from PySide6.QtCore import QObject, Signal
from browser import Browser
from time import sleep

class Worker(QObject):
    """
    Worker responsável por executar o processo de download dos arquivos DCTF em uma thread separada.

    Gerencia o ciclo de execução, sinais de progresso, controle de cancelamento e tratamento de erros.
    """
    wait_sec = 2
    ready = False
    end = Signal()
    conclusion = Signal(str)
    start = Signal()
    error = Signal(list)
    progress_bar = Signal(int)
    can_continue = Signal()
    session_err_msg = 'O navegador a ser usado foi fechado, o procedimento será reiniciado.. favor não fechar o navegador'
    is_started = False
    is_canceled = False

    def __init__(self, download_path: str, start_date: str, end_date: str) -> None:
        """
        Inicializa o worker com o caminho de download e intervalo de datas.
        """
        super().__init__()
        self.download_path = download_path
        self.start_date = start_date
        self.end_date = end_date
        pass

    def execute(self):
        """
        Executa o fluxo principal de download, emitindo sinais conforme o progresso.
        """
        try:
            self.browser = Browser(self.download_path)
            self.can_continue.emit()
            self._wait_confirm(self.browser)
            if self.is_canceled: return self.end.emit()

            self.browser.ecac()
            self.can_continue.emit()
            self._wait_confirm(self.browser)
            if self.is_canceled: return self.end.emit()

            self.start.emit()
            self.is_started = True
            self.browser.download_files(self.start_date, self.end_date)
            self.browser.chrome_reset()
            self.browser.close()
            # self.can_continue.emit()
            self.conclusion.emit(self.download_path)
        except Exception as err:
            self.browser.close()
            self.error.emit([err, self.is_started])
        finally:
            self.end.emit()

    def _wait_confirm(self, ecac: Browser):
        """
        Aguarda confirmação do usuário para prosseguir, verificando se o processo foi cancelado.
        """
        while self.ready == False and self.is_canceled == False:
            ecac.is_alive()
            sleep(self.wait_sec)
        self.ready = False

    def confirm(self): 
        """
        Sinaliza que o usuário confirmou a etapa atual.
        """
        self.ready = True

    def stop(self): 
        """
        Cancela a execução do worker.
        """
        if self.is_started:
            self.browser.cancel()
        else:
            self.is_canceled = True