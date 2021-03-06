#! /usr/bin/python3.6

import os

from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtGui import QIcon

from .info import __author_email__, __author__, __version__, __url__, __description__, __name__
from .read_shortcuts import populate_shortcuts, load_json
from .gui.catia_launcher_gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('catia_launcher/images/icon.png'))

        self.json_data = load_json()
        self.shortcut_links = populate_shortcuts(self.json_data)

        self.catia_selection = self.ui.combo_select_catia
        for link in self.shortcut_links:
            self.catia_selection.addItem(link.application_string)

        # start catia
        self.ui.btn_start_catia.clicked.connect(self.btn_start_catia_pressed)

        # exit application
        self.ui.btn_exit.clicked.connect(self.btn_exit_pressed)

        # open folders
        self.ui.btn_open_folders.clicked.connect(self.btn_open_folders_pressed)

        self.ui.actionAbout.triggered.connect(self.show_about)

    # starting catia
    def btn_start_catia_pressed(self):
        if self.catia_selection.currentIndex():
            self.shortcut_links[self.catia_selection.currentIndex() - 1].start_application()
        else:
            self.warning_message_box('Please select Application.')

    # opening folders
    def btn_open_folders_pressed(self):

        catia_settings = None
        if self.catia_selection.currentIndex():

            shortcut = self.shortcut_links[self.catia_selection.currentIndex() - 1]

            if hasattr(shortcut, "env"):
                catia_settings = shortcut.get_settings()
            else:
                self.warning_message_box('Please select CATIA application.')
        else:
            self.warning_message_box('Please select CATIA application.')

        if catia_settings:
            if self.ui.checkbox_temp_files.isChecked():
                os.startfile(catia_settings.cat_temp)
            if self.ui.checkbox_user_files.isChecked():
                os.startfile(catia_settings.cat_user_setting_path)

    def show_about(self):
        text = """<h1>{}</h1>
               <p>
               {}<br>
            Version: {}<br>
            Created by <a href="mailto: {}">{}</a>.<br>
            Source Code: <a href="{}">GitHub</a><br>
            License:  This application is distributed under the open source
            <a href="https://github.com/evereux/catia_launcher/blob/master/LICENSE">GNU General Public License v3.0</a>.
            This and the licensing restrictions of the open source 
            <a href="https://doc.qt.io/qtforpython/licenses.html#">PySide2</a> license should be considered before 
            modifying this code.
        </p>""".format(__name__, __description__, __version__, __author_email__, __author__, __url__)
        QMessageBox.information(self, "Information", text)

    def btn_exit_pressed(self):
        self.close()

    def warning_message_box(self, text="This is a warning"):
        QMessageBox.warning(self, "Warning", text)
