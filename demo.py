#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import QApplication

from pyqterm import TerminalWidget


if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = TerminalWidget()
	win.show()
	app.exec_()

