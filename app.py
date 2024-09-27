import sys
import time
import pyautogui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit

class MouseTrackerApp(QMainWindow):
    cantidad = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.positions = []

    def initUI(self):
        self.setWindowTitle('Mouse Tracker')
        self.setGeometry(100, 100, 500, 200)  # Increase width by 200 pixels

        self.button2 = QPushButton('Run', self)
        self.button2.clicked.connect(self.trabaja)

        self.text_input = QLineEdit(self)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button2)
        h_layout.addWidget(self.text_input)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    #definimos una funcion que acepta un int y lo imprime  
    def suma(self, cantidad):
        self.cantidad = str(cantidad)
        cantidad=str(100)
        pyautogui.moveTo(114, 497, duration=2)
        pyautogui.click()
        pyautogui.moveTo(1583, 293, duration=2)
        pyautogui.click()
        pyautogui.moveTo(829, 344, duration=2)
        pyautogui.click()
        pyautogui.typewrite('xrp', interval=0.5)  # useful for entering text, newline is Enter
        pyautogui.moveTo(859, 418, duration=2)
        pyautogui.click()
        pyautogui.moveTo(1143, 349, duration=2)
        pyautogui.click()
        pyautogui.moveTo(864, 689, duration=2)
        pyautogui.click()
        pyautogui.typewrite(cantidad, interval=0.5)  # useful for entering text, newline is Enter
        pyautogui.moveTo(951, 862, duration=2)
        pyautogui.click()


    def trabaja(self):
        # abre el navegador y entra a la pagina https://coinmarketcap.com/portfolio-tracker/
        pyautogui.hotkey('win', 'r')
        time.sleep(1)
        pyautogui.typewrite('chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite('https://coinmarketcap.com/portfolio-tracker/')
        pyautogui.press('enter')

        self.suma(self.text_input.text())



        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTrackerApp()
    ex.show()
    sys.exit(app.exec_())