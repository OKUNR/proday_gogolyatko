from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QRadioButton
app = QApplication([])
win = QWidget()
win.setWindowTitle("Конкурс від Crazy People")
win.resize(400, 200)
question = QLabel(win)
question.setText("Якого року канал отримав золоту кнопку від Ютуб?")
question.move(50, 10)
button1 = QRadioButton(win)
button1.setText("2005")
button1.move(100, 60)

button2 = QRadioButton(win)
button2.setText("2015")
button2.move(200, 60)

button3 = QRadioButton(win)
button3.setText("2000")
button3.move(100, 100)

button4 = QRadioButton(win)
button4.setText("2020")
button4.move(200, 100)

def OKUN():
    win2 = QMessageBox()
    win2.setText("Правильно! Ви виграли Гоголятко.")
    win2.exec_()

button3.clicked.connect(OKUN)

def trup_sigmi():
    win3 = QMessageBox()
    win3.setText("Неправильно! Правильна відповідь: 2000. Ви виграли Креветку.")
    win3.exec_()

button1.clicked.connect(trup_sigmi)
button2.clicked.connect(trup_sigmi)
button4.clicked.connect(trup_sigmi)

win.show()
app.exec_()
