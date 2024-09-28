import sys  # Importa el módulo sys para interactuar con el sistema
import time  # Importa el módulo time para manejar tiempos y pausas
import pyautogui  # Importa el módulo pyautogui para controlar el mouse y el teclado
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
# Importa los widgets necesarios de PyQt5 para crear la interfaz gráfica

class MouseTrackerApp(QMainWindow):  # Define una clase llamada MouseTrackerApp que hereda de QMainWindow
    cantidad = 0  # Variable de clase para almacenar una cantidad
    def __init__(self):  # Método constructor de la clase
        super().__init__()
        self.initUI()  # Llama al método initUI para inicializar la interfaz de usuario
        self.positions = []  # Inicializa una lista vacía para almacenar posiciones del mouse

    def initUI(self):  # Método para inicializar la interfaz de usuario
        self.setWindowTitle('Mouse Tracker')  # Establece el título de la ventana
        self.setGeometry(100, 100, 500, 200)  # Establece la posición y el tamaño de la ventana

        self.button2 = QPushButton('Run', self)  # Crea un botón con el texto 'Run'
        self.button2.clicked.connect(self.trabaja)  # Conecta el clic del botón al método trabaja

        self.text_input = QLineEdit(self)  # Crea una caja de texto para entrada de usuario

        h_layout = QHBoxLayout()  # Crea un layout horizontal
        h_layout.addWidget(self.button2)  # Agrega el botón al layout horizontal
        h_layout.addWidget(self.text_input)  # Agrega la caja de texto al layout horizontal

        layout = QVBoxLayout()  # Crea un layout vertical
        layout.addLayout(h_layout)  # Agrega el layout horizontal al layout vertical

        container = QWidget()  # Crea un widget contenedor
        container.setLayout(layout)  # Establece el layout del contenedor
        self.setCentralWidget(container)  # Establece el contenedor como el widget central de la ventana

    def suma(self, cantidad):  # Método para sumar una cantidad
        self.cantidad = str(cantidad)  # Convierte la cantidad a cadena y la almacena en la variable de clase
        cantidad = str(100)  # Asigna el valor '100' a la variable cantidad (como cadena)
        pyautogui.moveTo(114, 497, duration=2)  # Mueve el mouse a la posición (114, 497) en 2 segundos
        pyautogui.click()  # Hace clic en la posición actual del mouse
        pyautogui.moveTo(1583, 293, duration=2)  # Mueve el mouse a la posición (1583, 293) en 2 segundos
        pyautogui.click()  # Hace clic en la posición actual del mouse
        pyautogui.moveTo(829, 344, duration=2)  # Mueve el mouse a la posición (829, 344) en 2 segundos
        pyautogui.click()  # Hace clic en la posición actual del mouse
        pyautogui.typewrite('xrp', interval=0.5)  # Escribe 'xrp' con un intervalo de 0.5 segundos entre cada carácter
        pyautogui.moveTo(859, 418, duration=2)  # Mueve el mouse a la posición (859, 418) en 2 segundos
        pyautogui.click()  # Hace clic en la posición actual del mouse
        pyautogui.moveTo(1143, 349, duration=2)  # Mueve el mouse a la posición (1143, 349) en 2 segundos
        pyautogui.click()  # Hace clic en la posición actual del mouse
        pyautogui.moveTo(864, 689, duration=2)  # Mueve el mouse a la posición (864, 689) en 2 segundos
        pyautogui.click()  # Hace clic en la posición actual del mouse
        pyautogui.typewrite(cantidad, interval=0.5)  # Escribe la cantidad con un intervalo de 0.5 segundos entre cada carácter
        pyautogui.moveTo(951, 862, duration=2)  # Mueve el mouse a la posición (951, 862) en 2 segundos
        pyautogui.click()  # Hace clic en la posición actual del mouse

    def trabaja(self):  # Método para realizar una tarea
        # Abre el navegador y entra a la página https://coinmarketcap.com/portfolio-tracker/
        pyautogui.hotkey('win', 'r')  # Presiona las teclas 'win' y 'r' al mismo tiempo para abrir el cuadro de diálogo Ejecutar
        time.sleep(1)  # Espera 1 segundo
        pyautogui.typewrite('firefox')  # Escribe 'firefox' para abrir el navegador Firefox
        pyautogui.press('enter')  # Presiona la tecla Enter
        time.sleep(2)  # Espera 2 segundos para que el navegador se abra
        pyautogui.typewrite('https://coinmarketcap.com/portfolio-tracker/')  # Escribe la URL de la página
        pyautogui.press('enter')  # Presiona la tecla Enter para ir a la página

        self.suma(self.text_input.text())  # Llama al método suma con el texto ingresado en la caja de texto

if __name__ == '__main__':  # Punto de entrada de la aplicación
    app = QApplication(sys.argv)  # Crea una instancia de QApplication
    ex = MouseTrackerApp()  # Crea una instancia de MouseTrackerApp
    ex.show()  # Muestra la ventana principal
    sys.exit(app.exec_())  # Inicia el bucle de eventos de la aplicación