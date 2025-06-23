from PySide6.QtCore import QObject, Signal
from ecac import ECAC
from time import sleep

class Worker(QObject):
    wait_sec = 2
    ready = False
    end = Signal()
    conclusion = Signal(str)
    start = Signal()
    error = Signal(str)
    progress_bar = Signal(int)

    def __init__(self, download_path: str) -> None:
        super().__init__()
        self.download_path = download_path
        pass

    def execute(self):
        try:
            ecac = ECAC()
            self._wait_confirm()
            ecac.hide()
            ecac.download_files()
            ecac.close()
            self.conclusion.emit(self.download_path)
        except Exception as err:
            ecac.close()
            self.error.emit(err)
        finally:
            self.end.emit()

    def _wait_confirm(self):
        while self.ready == False:
            sleep(self.wait_sec)

    def confirm(self): 
        self.ready = True
        self.start.emit()