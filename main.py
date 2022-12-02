from controller import *

def main() -> None:
    '''
    Runs the GUI
    :return: Does not return anything
    '''
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()

if __name__ =='__main__':
    main()