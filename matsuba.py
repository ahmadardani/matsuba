import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from guiprogram_ui import Ui_MainWindow  # your pyuic5-generated UI file

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ✅ KDE global menu workaround for PyQt5 (if needed)
        self.setMenuBar(self.ui.menubar)

        self.ui.btnMenuExtract.clicked.connect(self.go_to_tab_1)
        self.ui.btnMenuGenerate.clicked.connect(self.go_to_tab_2)

    def go_to_tab_1(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def go_to_tab_2(self):
        self.ui.tabWidget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
