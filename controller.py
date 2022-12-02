from PyQt5.QtWidgets import *
from view import *
import random

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        '''
        Defines how the GUI will be set up and function
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(500, 500)
        global compBox, guess
        compBox = 0
        guess = 0
        self.randomRestart()
        self.Button1.clicked.connect(lambda: self.boxSelect(1))
        self.Button2.clicked.connect(lambda: self.boxSelect(2))
        self.Button3.clicked.connect(lambda: self.boxSelect(3))
        self.Button4.clicked.connect(lambda: self.boxSelect(4))
        self.Button5.clicked.connect(lambda: self.boxSelect(5))
        self.Button6.clicked.connect(lambda: self.boxSelect(6))
        self.Button7.clicked.connect(lambda: self.boxSelect(7))
        self.Button8.clicked.connect(lambda: self.boxSelect(8))
        self.Button9.clicked.connect(lambda: self.boxSelect(9))
        self.Button10.clicked.connect(lambda: self.boxSelect(10))
        self.Button11.clicked.connect(lambda: self.boxSelect(11))
        self.Button12.clicked.connect(lambda: self.boxSelect(12))
        self.Button13.clicked.connect(lambda: self.boxSelect(13))
        self.Button14.clicked.connect(lambda: self.boxSelect(14))
        self.Button15.clicked.connect(lambda: self.boxSelect(15))
        self.Button16.clicked.connect(lambda: self.boxSelect(16))
        self.Button17.clicked.connect(lambda: self.boxSelect(17))
        self.Button18.clicked.connect(lambda: self.boxSelect(18))
        self.Button19.clicked.connect(lambda: self.boxSelect(19))
        self.Button20.clicked.connect(lambda: self.boxSelect(20))
        self.Button21.clicked.connect(lambda: self.boxSelect(21))
        self.Button22.clicked.connect(lambda: self.boxSelect(22))
        self.Button23.clicked.connect(lambda: self.boxSelect(23))
        self.Button24.clicked.connect(lambda: self.boxSelect(24))
        self.Button25.clicked.connect(lambda: self.boxSelect(25))
        self.restartButton.clicked.connect(lambda: self.randomRestart())

    def randomRestart(self) -> None:
        '''
        Resets the UI back to it's initial conditions and randomizes the selection value
        :return: Does not return anything
        '''
        globalList = globals()
        globalList['compBox'] = random.randint(1, 25)
        globalList['guess'] = 0
        self.hotLabel.setVisible(False)
        self.coldLabel.setVisible(False)
        self.winLabel.setVisible(False)
        self.guessLabel.setVisible(False)
        self.restartButton.setVisible(False)

    def boxSelect(self, select: int) -> None:
        '''
        Determines UI adjustments depending on the user's given selection
        :param select: The integer value that the user is guessing
        :return: Does not return anything
        '''
        globalList = globals()
        globalList['guess'] += 1
        self.guessLabel.setText(str(guess))
        self.guessLabel.setVisible(True)
        if select == compBox:
            self.hotLabel.setVisible(False)
            self.coldLabel.setVisible(False)
            self.restartButton.setVisible(True)
            self.winLabel.setVisible(True)
            self.guessLabel.setVisible(False)
        elif compBox % 5 == 1:
            if compBox - 5 <= select <= compBox - 4 or select == compBox + 1 or compBox + 5 <= select <= compBox + 6:
                self.hotLabel.setVisible(True)
                self.coldLabel.setVisible(False)
            else:
                self.hotLabel.setVisible(False)
                self.coldLabel.setVisible(True)
        elif compBox % 5 == 0:
            if compBox - 6 <= select <= compBox - 5 or select == compBox - 1 or compBox + 4 <= select <= compBox + 5:
                self.hotLabel.setVisible(True)
                self.coldLabel.setVisible(False)
            else:
                self.hotLabel.setVisible(False)
                self.coldLabel.setVisible(True)
        else:
            if compBox - 6 <= select <= compBox - 4 or compBox - 1 <= select <= compBox + 1 or compBox + 4 <= select <= compBox + 6:
                self.hotLabel.setVisible(True)
                self.coldLabel.setVisible(False)
            else:
                self.hotLabel.setVisible(False)
                self.coldLabel.setVisible(True)