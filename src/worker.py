from PySide6.QtCore import QObject, Signal
from ecac import ECAC
from time import sleep

class Worker(QObject):
    wait_sec = 2
    
    def __init__(self, download_path: str) -> None:
        self.download_path = download_path
        pass

    def execute(self):
        ecac = ECAC()
        self._wait_confirm()
        ecac.hide()
        ecac.download_files()
        ecac.close()

    def _wait_confirm(self):
        while self.confirm == False:
            sleep(self.wait_sec)

    def confirm(self): self.confirm = True