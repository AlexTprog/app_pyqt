import mysql.connector
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class main_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui",self)
        self.consultar.clicked.connect(self.fn_consultar)

    def fn_consultar(self):
        try:
            conex = mysql.connector.connect(
                user="root",
                password="12345",
                host="localhost",
                database="pruebas",
                port="3306"
            )

            if conex.is_connected():
                print("Conexion exitosa")

                info_server = conex.get_server_info()
                print(info_server)
                cursor = conex.cursor()
                cursor.execute("SELECT * FROM FAMILIA WHERE DNI = {}".format(self.input_dni.text()))

                for (DNI, NOMBRES, APELLIDO_PATERNO, APELLIDO_MATERNO, FECHA_NACIMIENTO) in cursor:
                    self.output_datos.setText("{} {} {} {}".format( NOMBRES, APELLIDO_PATERNO, APELLIDO_MATERNO, FECHA_NACIMIENTO))

            conex.close()
        except Exception() as ex:
            print(ex)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = main_GUI()
    GUI.show()
    sys.exit(app.exec_())


