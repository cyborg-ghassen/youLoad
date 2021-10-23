import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
from Classes.func import Functions
from pytube import YouTube, Playlist


def getFiles(line):
    fileName = QFileDialog.getExistingDirectory(caption='Choose Directory', directory=QDir.rootPath())
    line.setText(fileName)


def xFounder():
    x = 800 / 2 - 300 / 2
    return x


def design():
    app = QApplication(sys.argv)
    window = QMainWindow()
    title = 'Youtube Downloader'
    app.setApplicationName(title)
    window.setGeometry(100, 150, 800, 600)
    ################################################
    #           LOGO                               #
    ################################################
    label = QLabel(window)
    logo = QPixmap('youLoad.png').scaled(100, 100)
    logo.isQBitmap()
    label.setPixmap(logo)
    label.resize(100, 100)
    label.setGeometry(30, 30, 100, 100)
    ################################################
    #           TITLE                              #
    ################################################
    l = QLabel("Youtube Downloader", window)
    l.setGeometry(xFounder(), 100, 300, 50)
    l.setStyleSheet("*{font-size: 32px;}")
    ################################################
    #           LABEL                              #
    ################################################
    choose = QLabel("Choose what to download: ", window)
    choose.setGeometry(xFounder(), 150, 300, 50)
    choose.setStyleSheet("*{font-size: 16px;}")
    ################################################
    #           COMBOBOX                           #
    ################################################
    type = QComboBox(window)
    type.setGeometry(450, 165, 100, 25)
    type.addItem("Video")
    type.addItem("Playlist")
    type.addItem("Audio")
    ################################################
    #           LABEL                              #
    ################################################
    l = QLabel("Enter link: ", window)
    l.setGeometry(100, 200, 100, 50)
    l.setStyleSheet("*{font-size: 18px;}")
    ################################################
    #           LINEEDIT                           #
    ################################################
    link = QLineEdit(window)
    link.setGeometry(250, 212, 300, 25)
    ################################################
    #           COMBOBOX                           #
    ################################################
    qual = QComboBox(window)
    qual.setGeometry(570, 212, 100, 25)
    qual.addItem("1080p")
    qual.addItem("720p")
    qual.addItem("480p")
    qual.addItem("360p")
    qual.addItem("240p")
    qual.addItem("144p")
    ################################################
    #           LABEL                              #
    ################################################
    place = QLabel("Choose where to save: ", window)
    place.setGeometry(100, 300, 200, 50)
    place.setStyleSheet("*{font-size: 14px;}")
    ################################################
    #           LINEEDIT                           #
    ################################################
    line = QLineEdit(window)
    line.setGeometry(250, 312, 300, 25)
    ################################################
    #           BROWSE                             #
    ################################################
    browse = QPushButton("Browse", window)
    browse.setGeometry(570, 312, 100, 25)
    if browse.clicked:
        browse.clicked.connect(lambda: getFiles(line))
    ################################################
    #           BUTTON                             #
    ################################################
    download = QPushButton("Download", window)
    download.setGeometry(400, 400, 100, 25)
    ################################################
    #           EXECUTE                            #
    ################################################
    func = Functions()
    if type.currentText() == "Video":
        download.clicked.connect(lambda: func.video(link.text(), qual.currentText(), line.text()))
    if type.currentText() == "Playlist":
        qual.setDisabled(True)
        try:
            p = Playlist(link.text())
            print("Downloading {}".format(p.title))
            for i in p.videos:
                print("{} - Downloading {}".format(i, i.title))
                stream = i.streams.get_highest_resolution()
                print(stream)
                stream.download(output_path=line.text() + p.title)
            print("Download completed")
        except Exception as e:
            print(e)
    if type.currentText() == "Audio":
        download.clicked.connect(lambda: func.audio(link.text(), qual.currentText(), line.text()))
    link.setText("")
    line.setText("")
    window.show()
    app.exec_()
