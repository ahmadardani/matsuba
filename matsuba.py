import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from guiprogram_ui import Ui_MainWindow  # your pyuic5-generated UI file
from anki_space_settings import AnkiSpaceSettingsWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMenuBar(self.ui.menubar)

        self.ui.btnMenuExtract.clicked.connect(self.go_to_tab_1)
        self.ui.btnMenuGenerate.clicked.connect(self.go_to_tab_2)
        self.ui.tabWidget.tabBar().hide()

        # ⛔ Don't create the settings window yet — wait until user clicks
        self.ui.actionConfigure_Anki_Separation_Space.triggered.connect(self.show_anki_settings)

    def go_to_tab_1(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def go_to_tab_2(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def show_anki_settings(self):
        # ✅ Safe to create window here (after QApplication is running)
        self.anki_settings_window = AnkiSpaceSettingsWindow()
        self.anki_settings_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
