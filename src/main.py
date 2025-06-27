from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy, QToolBar
)
from PySide6.QtGui import QPixmap, QIcon, QMovie, QAction
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
from pathlib import Path

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Classe principal da interface gráfica do sistema, responsável por interagir com o usuário e orquestrar as operações.

    Esta classe gerencia a navegação entre telas, coleta de dados do usuário, inicialização e controle do worker de download,
    além de exibir mensagens e controlar o fluxo da aplicação.
    """
    step = Step()
    worker = None
    complete_msg = 'Todos arquivos DCTF WEB foram baixados com êxito, a pasta que destinou o download será aberta após o "ok"'
    back_msg = 'Retrosseda os passos até alcançar a tela indicada, caso a dificuldade persista, consulte os responsáveis'
    is_ready_msg = 'Confirma ter alcançado a tela indicada pelas instrunções?'
    warning_auto = 'Uma operação automática irá iniciar, NÃO USE o mouse e teclado até que a próxima instrunção apareça'
    DATE_INDEX = 1
    MAIN_INDEX = 0
    ico_path = Path(__file__).parent / 'imgs' / 'icon_downloader.ico'

    def __init__(self, parent = None) -> None:
        """
        Inicializa a janela principal e conecta os sinais aos slots.
        """
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon(self.ico_path.__str__()))

        menu = self.menuBar()
        reset_menu = menu.addMenu('&Funções Extra')

        new_action = QAction("Reiniciar", self)
        new_action.triggered.connect(self.reset)
        reset_menu.addAction(new_action)

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

        self.current_connection =\
            self.pushButton_execute.clicked.connect(self.send)
        self.pushButton_back.clicked.connect(lambda: self.send(1))
        self.pushButton_jump.clicked.connect(lambda: self.send(2))

        self.pushButton_send_date.clicked.connect(self.request_date)
        self.pushButton_cancel_date.clicked.connect(self.cancel_date)
        
        self.reset()

    def send(self, value = 0):
        """
        Atualiza a interface com a próxima instrução ou executa a ação correspondente.
        """
        func = self.ref[value]
        label, instruction = func()
        
        self.label_instruction.setText(instruction)
        self.pushButton_execute.setText(label)
        
        if self.step.is_execution_time(): self.execute()

    def reset(self):
        """
        Reinicia o fluxo da aplicação, resetando o worker e a navegação.
        """
        if self.worker != None:
            self.worker.stop()
            self.worker = None

            # self.disable_bttns()

        self.stackedWidget.setCurrentIndex(self.MAIN_INDEX)
        self.step.start()
        self.send()

    def execute(self):
        """
        Inicia o processo de download, alternando para a tela de datas ou aguardando confirmação do usuário.
        """
        if self.worker == None:
            self.stackedWidget.setCurrentIndex(self.DATE_INDEX)
        else:
            self.disable_bttns()
            if askyesno('Aviso', self.is_ready_msg):
                showwarning('CUIDADO', self.warning_auto)
                self.worker.confirm()
            else:
                showinfo('Aviso', self.back_msg)
                self.send(1)
                self.disable_bttns()
    
    def request_date(self):
        """
        Solicita as datas de início e fim do usuário e o diretório de download.
        """
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
        finally:
            self.stackedWidget.setCurrentIndex(self.MAIN_INDEX)

    def request_path(self):
        """
        Abre um diálogo para o usuário selecionar o diretório de download.
        """
        self.disable_bttns()
        path = askdirectory()
        if path == '': raise Exception('Operação cancelada')
        return path

    def cancel_date(self):
        """
        Cancela a seleção de datas e retorna à tela principal.
        """
        self.reset()
        self.stackedWidget.setCurrentIndex(self.MAIN_INDEX)
        showwarning(title='Aviso', message='Operação cancelada')
        
    def to_continue(self):
        """
        Avança para a próxima instrução e desabilita os botões.
        """
        self.send()
        self.disable_bttns()

    def disable_bttns(self):
        """
        Habilita ou desabilita os botões de navegação conforme o estado atual.
        """
        state = True if self.pushButton_execute.isEnabled() else False
        for i in self.to_disable: i.setDisabled(state)

    def open(self, path):
        """
        Inicializa o worker e a thread para realizar o download dos arquivos.
        """
        self.worker = Worker(
            path,
            self.dateEdit_2.text(),
            self.dateEdit_end.text()
        )
        self._thread = QThread()

        self.worker.moveToThread(self._thread)
        self._thread.started.connect(self.worker.execute)
        self.worker.end.connect(self._thread.quit)
        self.worker.end.connect(self._thread.deleteLater)
        self.worker.start.connect(self.start)
        self.worker.error.connect(self.error)
        self.worker.conclusion.connect(self.conclusion)
        self.worker.can_continue.connect(self.to_continue)
        # self._thread.finished.connect(self.worker.deleteLater)
        self._thread.start()

    def start(self):
        """
        Atualiza a interface para o estado de execução e conecta o botão de execução ao cancelamento.
        """
        self.send()
        self.pushButton_execute.disconnect(self.current_connection)
        self.current_connection =\
            self.pushButton_execute.clicked.connect(self.cancel)
        self.pushButton_execute.setDisabled(False)
    
    def conclusion(self, path):
        """
        Exibe mensagem de conclusão e abre o diretório de download.
        """
        self.switch_execute()
        self.disable_bttns()
        self.reset()
        showinfo(title='Aviso', message= self.complete_msg)
        startfile(path)

    def error(self, result: list[str, bool]):
        """
        Exibe mensagem de erro e reinicia o fluxo.
        """
        message, reset = result
        if reset: self.switch_execute()
        self.reset()
        showwarning(title='Aviso', message= message)

    def switch_execute(self):
        """
        Alterna a conexão do botão de execução entre enviar e cancelar.
        """
        self.pushButton_execute.disconnect(self.current_connection)
        self.current_connection =\
            self.pushButton_execute.clicked.connect(self.send)
        
    def cancel(self):
        """
        Cancela a operação em andamento.
        """
        self.send()
        self.pushButton_execute.setDisabled(True)
        self.worker.stop()

if __name__ == '__main__':
    # Inicializa a aplicação Qt.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()