from PySide6.QtCore import QObject, Signal
from selenium.common.exceptions import InvalidSessionIdException
from ecac import ECAC
from time import sleep

class Worker(QObject):
    wait_sec = 2
    ready = False
    end = Signal()
    conclusion = Signal(str)
    start = Signal()
    error = Signal(list)
    progress_bar = Signal(int)
    session_err_msg = 'O navegador a ser usado foi fechado, o procedimento será reiniciado.. favor não fechar o navegador'

    def __init__(self, download_path: str) -> None:
        super().__init__()
        self.download_path = download_path
        pass

    def execute(self):
        try:
            ecac = ECAC()
            self._wait_confirm(ecac)
            ecac.hide()
            ecac.download_files()
            ecac.close()
            self.conclusion.emit(self.download_path)
        except InvalidSessionIdException:
            in_execution = True if self.ready else False
            self.error.emit([self.session_err_msg, in_execution])
        except Exception as err:
            ecac.close()
            in_execution = True if self.ready else False
            self.error.emit([err, in_execution])
        finally:
            self.end.emit()

    def _wait_confirm(self, ecac: ECAC):
        while self.ready == False:
            ecac.is_alive()
            sleep(self.wait_sec)

    def confirm(self): 
        self.ready = True
        self.start.emit()