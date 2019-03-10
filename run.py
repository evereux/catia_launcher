#! /usr/bin/python3.6

import os
import sys

from PySide2.QtWidgets import QApplication

from catia_launcher.json_tools import create_config, json_file
from catia_launcher import MainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
