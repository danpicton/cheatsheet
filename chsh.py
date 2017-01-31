import sys
from PyQt4 import QtGui, QtCore


class mymainwindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(QtGui.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
            QtCore.QSize(640, 480),
            QtGui.qApp.desktop().availableGeometry())
        )
        self.setWindowOpacity(0.9)
        self.setStyleSheet('QMainWindow{background-color: darkgray; border: 5px solid darkgray}')
        self.label = QtGui.QLabel(self)
        self.label.setText('cats')

    def mousePressEvent(self, event):
        QtGui.qApp.quit()

app = QtGui.QApplication(sys.argv)
mywindow = mymainwindow()
mywindow.show()
app.exec_()
