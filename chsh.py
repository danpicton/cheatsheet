import sys
from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import QWebView
#from PyQt4.QtGui import QApplication
#from PyQt4.QtCore import QUrl

html = '''
<html>
<head>
<title>A Sample Page</title>
</head>
<body style="background-image:url({url})">
<h1>Hello, World!</h1>
<hr />
I have nothing to say.
</body>
</html>
'''.format(url=QUrl("qrc:///home/dan/Projects/cheatsheet/splash_loading.jpg"))

class myWebView(QtWebKit.QWebView):
    def __init__(self):
        QtWebKit.QWebView.__init__(self)
        #self.load(QUrl("https://www.google.co.uk/"))
        self.setHtml(html)
        self.setWindowOpacity(0.9)
        radius = 10.0
        path = QtGui.QPainterPath()
        self.resize(640,480)
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        self.move(QtGui.QCursor.pos())
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
        self.setStyleSheet('QWebView{background-color: darkgray; border: 5px solid darkgray}')

    def mousePressEvent(self, event):
        QtGui.qApp.quit()

app = QtGui.QApplication(sys.argv)
browser = myWebView()
browser.show()
app.exec_()
