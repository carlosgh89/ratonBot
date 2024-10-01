import sys
import time
import pyautogui
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QFileDialog

class MouseTrackerApp(QMainWindow):
    cantidad = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        self.positions = []
        self.excel_file = ""

    def initUI(self):
        self.setWindowTitle('ENtradas Auto')
        self.setGeometry(100, 100, 500, 300)  # Increase width by 200 pixels and height by 100 pixels

        self.button2 = QPushButton('Añade un valor', self)
        self.button2.clicked.connect(self.trabaja)

        self.text_input = QLineEdit(self)

        self.file_button = QPushButton('Selecciona archivo Excel', self)
        self.file_button.clicked.connect(self.select_file)

        self.process_button = QPushButton('Process Excel File', self)
        self.process_button.clicked.connect(self.process_excel_file)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button2)
        h_layout.addWidget(self.text_input)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(self.file_button)
        layout.addWidget(self.process_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def suma(self, cantidad):
        cantidad = str(cantidad)
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
        pyautogui.typewrite('cmd')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite('start chrome /MAX https://coinmarketcap.com/portfolio-tracker/')
        pyautogui.press('enter')
        time.sleep(5)

        self.suma(self.text_input.text())

    def trabajaGrupo(self, listaEntradas):
        # abre el navegador y entra a la pagina https://coinmarketcap.com/portfolio-tracker/
        pyautogui.hotkey('win', 'r')
        time.sleep(1)
        pyautogui.typewrite('cmd')
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.typewrite('start chrome /MAX https://coinmarketcap.com/portfolio-tracker/')
        pyautogui.press('enter')
        time.sleep(5)
        for i in listaEntradas:
            self.suma(i)
            time.sleep(2)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xlsx *.xls)", options=options)
        if file_name:
            self.excel_file = file_name
            print(f"Selected file: {self.excel_file}")

    def process_excel_file(self):
        if self.excel_file:
            lista_numeros = self.obtener_lista_numeros(self.excel_file)
            print(f"Numbers from Excel: {lista_numeros}")
            self.trabajaGrupo(lista_numeros)
        else:
            print("No file selected")

        #vamos a iterar sobre la lista de numeros 

    def obtener_lista_numeros(self, archivo_excel):
        # Lee el archivo de Excel
        df = pd.read_excel(archivo_excel, usecols="A", skiprows=1, nrows=9)
        # Obtiene la lista de números desde el rango A2:A10
        lista_numeros = df.iloc[:, 0].tolist()
        return lista_numeros

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTrackerApp()
    ex.show()
    sys.exit(app.exec_())