from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QColor

app = QApplication([])
window = QWidget()

layout = QVBoxLayout()

label = QLabel("Merhaba, PyQt ile gelişmiş bir arayüz!")
layout.addWidget(label)

button1 = QPushButton("Buton 1")
layout.addWidget(button1)

button2 = QPushButton("Buton 2")
layout.addWidget(button2)

def change_background_color():
    color = QColor(255, 0, 0)  # Kırmızı renk
    window.setStyleSheet(f"background-color: {color.name()};")

button1.clicked.connect(change_background_color)

def change_label_text():
    label.setText("Buton 2'ye tıklandı!")

button2.clicked.connect(change_label_text)

window.setLayout(layout)
window.show()

app.exec_()
