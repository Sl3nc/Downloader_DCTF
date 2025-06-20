from PySide6.QtWidgets import (
    QMainWindow, QApplication, QCheckBox, QTreeWidgetItem, QPushButton, QHBoxLayout, QFrame, QSizePolicy
)
from PySide6.QtGui import QPixmap, QIcon, QMovie
from tkinter.filedialog import askopenfilename
from window_downloader_dctf import Ui_MainWindow
from PySide6.QtCore import QThread, QSize
from step import Step

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Classe principal da interface gráfica do sistema, responsável por interagir com o usuário e orquestrar as operações.
    """
    step = Step()
    def __init__(self, parent = None) -> None:
        """
        Inicializa a janela principal e conecta os sinais aos slots.
        """
        super().__init__(parent)
        self.setupUi(self)

        self.ref = {
            0: lambda: self.step.next(),
            1: lambda: self.step.back(),
            2: lambda: self.step.jump()
        }

        self.pushButton_execute.clicked.connect(self.send)
        self.pushButton_back.clicked.connect(lambda: self.send(1))
        self.pushButton_jump.clicked.connect(lambda: self.send(2))
        
        label, instruction = self.step()
        self.label_instruction.setText(instruction)
        self.pushButton_execute.setText(label)

    #Executado pelo enviar / prosseguir
    def send(self, value = 0):
        func = self.ref[value]
        label, instruction = func()
        
        self.label_instruction.setText(instruction)
        self.pushButton_execute.setText(label)
        
        #Receber texto do botão também
        #Define o result como valor da instrunção

if __name__ == '__main__':
    # Inicializa a aplicação Qt.
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()