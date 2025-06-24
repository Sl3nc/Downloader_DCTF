from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy
)
from PySide6.QtGui import QPixmap, QIcon, QMovie
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning, showinfo, askyesno
from window_downloader_dctf import Ui_MainWindow
from PySide6.QtCore import QThread, QSize, QDate
from step import Step
from worker import Worker
from os import startfile
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Classe principal da interface gráfica do sistema, responsável por interagir com o usuário e orquestrar as operações.
    """
    step = Step()
    worker = None
    complete_msg = 'Todos arquivos DCTF WEB foram baixados com êxito, a pasta que destinou o download será aberta após o "ok"'
    no_find_msg = 'Retrosseda os passos até alcançar a tela indicada, caso a dificuldade persista, consulte os responsáveis'
    is_find_msg = 'Confirma ter alcançado a tela indicada pelas instrunções?'
    warning_auto = 'Uma operação automática irá iniciar, NÃO USE o mouse e teclado até que a próxima instrunção apareça'
    DATE_INDEX = 1
    LOAD_INDEX = 2
    MAIN_INDEX = 0

    def __init__(self, parent = None) -> None:
        """
        Inicializa a janela principal e conecta os sinais aos slots.
        """
        super().__init__(parent)
        self.setupUi(self)

        now = datetime.now()
        self.dateEdit_end.setDate(now)
        self.dateEdit_2.setDate(now  - relativedelta(months=1))

        self.ref = {
            0: lambda: self.step.next(),
            1: lambda: self.step.back(),
            2: lambda: self.step.jump()
        }

        self.to_disable = [
            self.pushButton_back,
            self.pushButton_execute,
            self.pushButton_jump
        ]

        self.pushButton_execute.clicked.connect(self.send)
        self.pushButton_back.clicked.connect(lambda: self.send(1))
        self.pushButton_jump.clicked.connect(lambda: self.send(2))

        self.pushButton_send_date.clicked.connect(self.request_date)
        self.pushButton_cancel_date.clicked.connect(self.cancel_date)
        
        self.reset()

    def send(self, value = 0):
        func = self.ref[value]
        label, instruction = func()
        
        self.label_instruction.setText(instruction)
        self.pushButton_execute.setText(label)
        
        if self.step.is_execution_time(): self.execute()

    def reset(self, was_started= False):
        if was_started == True:
            self.load_progress()

        self.worker = None
        self.step.start()
        self.send()

    def execute(self):
        if self.worker == None:
            self.stackedWidget.setCurrentIndex(self.DATE_INDEX)
        else:
            if askyesno('Aviso', self.is_find_msg):
                showwarning('CUIDADO', self.warning_auto)
                self.worker.confirm()
                self.send()
            else:
                showinfo('Aviso', self.no_find_msg)
                self.send(1)
    
    def request_date(self):
        try:
            date_start = date(*self.dateEdit_2.date().getDate())
            date_end = date(*self.dateEdit_end.date().getDate())
            if date_end < date_start:
                raise Exception('Operção cancelada')
            
            path = self.request_path()
            showwarning('CUIDADO', self.warning_auto)
            self.open(path)
        except Exception as err:
            self.reset()
            self.disable_bttns()
            showwarning(title='Aviso', message=err)

    def request_path(self):
        self.disable_bttns()
        path = askdirectory()
        if path == '': raise Exception('Operação cancelada')
        return path

    def cancel_date(self):
        self.reset()
        self.disable_bttns()
        showwarning(title='Aviso', message='Operação cancelada')
        
    def to_continue(self):
        self.send()
        self.disable_bttns()

    def disable_bttns(self):
        state = True if self.pushButton_execute.isEnabled() else False
        for i in self.to_disable: i.setDisabled(state)


    def open(self, path):
        self.worker = Worker(
            path,
            self.dateEdit.text(),
            self.dateEdit_2.text()
        )
        self._thread = QThread()

        self.worker.moveToThread(self._thread)
        self._thread.started.connect(self.worker.execute)
        self.worker.end.connect(self._thread.quit)
        self.worker.end.connect(self._thread.deleteLater)
        self.worker.start.connect(self.load_progress)
        self.worker.error.connect(self.error)
        self.worker.conclusion.connect(self.conclusion)
        self.worker.can_continue.connect(self.to_continue)
        self.worker.progress_bar.connect(self.to_progress)
        # self._thread.finished.connect(self.worker.deleteLater)
        self._thread.start()
    
    def to_progress(self, value):
        """
        Atualiza o valor da barra de progresso.
        """
        self.progressBar.setValue(value)

    def conclusion(self, path):
        self.reset(True)
        showinfo(title='Aviso', message= self.complete_msg)
        startfile(path)

    def error(self, result: list[str, bool]):
        message, reset = result
        self.reset(reset)
        showwarning(title='Aviso', message= message)

    def load_progress(self):
        """
        Controla a exibição do carregamento geral.
        """
        value = self.LOAD_INDEX if self.stackedWidget.currentIndex() == self.MAIN_INDEX else self.MAIN_INDEX
        self.stackedWidget.setCurrentIndex(value)

if __name__ == '__main__':
    # Inicializa a aplicação Qt.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()