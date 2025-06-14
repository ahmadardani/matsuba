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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
