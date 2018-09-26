import sys
import time
from PyQt4 import QtGui, QtCore
from zipfile import ZipFile
import os
from collections import defaultdict, Iterable, OrderedDict
import rdflib
import pprint


class application(QtGui.QApplication):

    class mainWidget(QtGui.QWidget):

        def __init__(self):

            QtGui.QWidget.__init__(self)

            self.layout = QtGui.QVBoxLayout(self)
            self.setLayout(self.layout)

            self.initUI()
            self.set_text("blablabla")

        def initUI(self):
            self.textField = QtGui.QTextEdit()
            self.layout.addWidget(self.textField)

        def load_file(self, f):

            None

        def set_text(self, t):

            self.textField.setText(t)

        def clear_text(self):

            self.textField.clear()

    class abstract_treeview(QtGui.QTreeWidget):

        """Base class for the two treeview controls"""

        ATTRIBUTES = ['Name']



        def __init__(self):
            QtGui.QTreeView.__init__(self)
            self.setColumnCount(len(self.ATTRIBUTES))
            self.setHeaderLabels(self.ATTRIBUTES)
            self.children = defaultdict(list)
            self.itemDoubleClicked.connect(self.testingThis)

        # def handler(self, column_no):
        #     #print(item, column_no)
        #     data = column_no.data(0,0).toString()
        #     super(application, self).mainWidget().clear_text()

        def testingThis(self, t):

            #print t.data(1, 1).toString()
            app.canvas.set_text(t.data(1, 1).toString())



        def load_file(self, f):

            root = QtGui.QTreeWidgetItem(self, [os.path.basename(f.filename)])
            dirs = {}

            for file in f.filelist:
                d = str(os.path.dirname(file.filename))
                fileName = str(os.path.basename(file.filename))
                if len(d) == 0:
                    fileTree = QtGui.QTreeWidgetItem(root, [fileName])
                    fileTree.setData(1, 1, self.read_zip(f, file))
                    #print fileTree.data(1, 1).toString()
                else:
                    if d in dirs:
                        fileTree = QtGui.QTreeWidgetItem(dirs[d], [fileName])
                        fileTree.setData(1, 1, self.read_zip(f, file))
                    else:
                        subdir = QtGui.QTreeWidgetItem(root, [d])
                        fileTree = QtGui.QTreeWidgetItem(subdir, [fileName])
                        dirs[d] = subdir
                        fileTree.setData(1, 1, self.read_zip(f, file))

        def read_zip(self, zip, file):

            handle = zip.open(file)
            data = handle.read()
            g = rdflib.Graph()
            if ".rdf" in str(file.filename):
               try:
                    p = g.parse(data= data)
                    string = ""
                    for stmt in g:
                        string += "\n" + str(stmt) + "\n"
                    #print (string + "<<<<<<<<<<<<")
                    data = string
               except:
                   print (file.filename + " not parsed")
            return data


                # fileName = str(os.path.basename(file.filename))
                # fileName = str(file.filename)
                # QtGui.QTreeWidgetItem(root, [fileName])

    class window(QtGui.QMainWindow):

        title = "ICDD Viewer"
        window_closed = QtCore.pyqtSignal([])

        def __init__(self):
            QtGui.QMainWindow.__init__(self)
            self.setWindowTitle(self.title)
            self.menu = self.menuBar()
            self.menus = {}

        def add_menu_item(self, menu, label, callback, icon=None, shortcut=None):
            m = self.menus.get(menu)
            if m is None:
                m = self.menu.addMenu(menu)
                self.menus[menu] = m

            if icon:
                a = QtGui.QAction(QtGui.QIcon(icon), label, self)
            else:
                a = QtGui.QAction(label, self)

            if shortcut:
                a.setShortcut(shortcut)

            a.triggered.connect(callback)
            m.addAction(a)

    def __init__(self):

        QtGui.QApplication.__init__(self, sys.argv)
        self.window = application.window()
        self.tree = application.abstract_treeview()
        self.canvas = application.mainWidget()
        self.window.showMaximized()

        # Adding Tabs to the Main Window

        self.tabs = QtGui.QTabWidget()
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(self.tabs)
        self.tabs.addTab(self.tree, 'ICDD Tree')
        splitter.setSizes([200, 600])
        self.window.setCentralWidget(splitter)

        splitter2 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter2.addWidget(self.canvas)
        splitter.addWidget(splitter2)
        splitter2.setSizes([400, 200])

        self.components = [self.tree, self.canvas]
        self.files = {}



        # Adding menu items to the bar

        self.window.add_menu_item('File','&Open',self.browseICDD,shortcut='CTRL+O')
        self.window.add_menu_item('File', '&Clear', self.clear, shortcut='CTRL+I')
        self.window.add_menu_item('File', '&Set Text', self.setText, shortcut='CTRL+T')
        # self.window.add_menu_item('File', '&Close', self.clear, shortcut='CTRL+W')
        self.window.add_menu_item('File', '&Exit', self.window.close, shortcut='ALT+F4')


        #self.settings = settings

    def start(self):
        self.window.show()
        sys.exit(self.exec_())

    def browseICDD(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.window, 'Open ICDD file', ".","Information container for data drop (*.ICDD)")
        self.load(filename)

    def load(self, fn):

        if fn in self.files:
            return

        f = ZipFile(str(fn))
        self.files[fn] = f

        # load file in every Component

        for c in self.components:
            #print (c)
            c.load_file(f)#, setting=self.settings)

    def clear(self):
        self.canvas.clear_text()

    def setText(self):
        self.canvas.set_text("blablabla2")

    def testingThis(object, t):

        print t





if __name__ == "__main__":
   app = application()
   app.start()

#
# for file in icdd_zip.filelist:
#     d = str(os.path.dirname(file.filename))
#     f = str(os.path.basename(file.filename))