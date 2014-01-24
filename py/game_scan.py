from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
from xml_creator import *

import sys, os, fnmatch

xml = XmlLibrary()

class ScanDirectory(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._scan = ""
        self._directory = ""
        self._extensions = ""

    @pyqtProperty('QString')
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, path):
        if "file:///" in path: #Qt adds this to found files.
            print(path)
            clean = path.strip("file:///")
            if PLATFORM != "win32":
                clean = "/" + clean
        else:
            clean = path
        print(clean)
        self._directory = clean
        
    @pyqtProperty('QString')
    def extensions(self):
        return self._extensions

    @extensions.setter
    def extensions(self, exts):
        self._extensions = exts

    @pyqtProperty('QString')
    def scan(self):
        print(self._directory)
        matches = {}
        for root, dirnames, filenames in os.walk(self._directory):
            for extension in ("*.sfc", "*.nes", "*.gba", "*.n64", "*.z64","*.cue" ):
                for filename in fnmatch.filter(filenames, extension):
                    matches[filename] = os.path.join(root, filename)
        if len(matches) == 0:
            return "Game files could not be found in the location."
        else:
            self._scan = matches
            xml.data = self._scan
            xmlwriter(xml.data)

