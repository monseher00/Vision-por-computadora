import cv2
import numpy as np
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QSlider, QVBoxLayout, QWidget,
                             QFileDialog, QMessageBox, QHBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QImage


class VentanaFiltroMediana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filtro de mediana")
        self.setGeometry(100, 100, 1000, 600)  #

        self.img = None
        self.img_filtrada = None

        # Botón para cargar la imagen
        self.btn_cargar = QPushButton("Cargar imagen")
        self.btn_cargar.clicked.connect(self.cargar_imagen)

        # Botón para aplicar el filtro
        self.btn_filtro = QPushButton("Aplicar filtro")
        self.btn_filtro.clicked.connect(self.aplicar_filtro)

        # Deslizador para ajustar el porcentaje del filtro
        self.sld_filtro = QSlider(Qt.Orientation.Horizontal)
        self.sld_filtro.setMinimum(0)
        self.sld_filtro.setMaximum(100)
        self.sld_filtro.setTickInterval(1)
        self.sld_filtro.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.sld_filtro.valueChanged.connect(self.actualizar_porcentaje)

        # Etiqueta para mostrar el porcentaje del filtro
        self.lbl_porcentaje = QLabel("Porcentaje: 0%")

        # Imagen original
        self.lbl_imagen_original = QLabel()
        #self.lbl_imagen_original.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Imagen filtrada
        self.lbl_imagen_filtrada = QLabel()
        #self.lbl_imagen_filtrada.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Diseño de la interfaz
        layout = QVBoxLayout()
        images = QHBoxLayout()
        layout.addWidget(self.btn_cargar)
        layout.addWidget(self.btn_filtro)
        layout.addWidget(self.sld_filtro)
        layout.addWidget(self.lbl_porcentaje)
        images.addWidget(self.lbl_imagen_original)
        images.addWidget(self.lbl_imagen_filtrada)
        layout.addLayout(images)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def cargar_imagen(self):
        file_dialog = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if file_dialog[0] != '':
            image_path = file_dialog
            # imagen original leìda con opencv
            self.img = cv2.imread(image_path[0])
            h, w, c = self.img.shape
            bytesPerLine = 3 * w

            # imagen en pixmap para colocar en label
            qImg = QImage(self.img.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
            self.lbl_imagen_original.setPixmap(QPixmap(qImg))

    def aplicar_filtro(self):
        if self.img is None:
            return 0

        porcentaje = self.sld_filtro.value()
        self.lbl_porcentaje.setText(f"Porcentaje: {porcentaje}%")

        # Aplicando el filtro de mediana con el porcentaje seleccionado
        ksize = int((porcentaje / 100) * 10) + 1
        if ksize % 2 == 0:
            ksize = ksize + 1
        if ksize < 3:
            ksize = 3

        self.img_filtrada = cv2.medianBlur(self.img, ksize)
        h, w, c = self.img_filtrada.shape
        bytesPerLine = 3 * w
        # imagen en pixmap para colocar en label
        qImg = QImage(self.img_filtrada.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)
        self.lbl_imagen_filtrada.setPixmap(QPixmap(qImg))

    def actualizar_porcentaje(self, valor):
        self.lbl_porcentaje.setText(f"Porcentaje: {valor}%")

"""
    def convertir_pixmap_a_numpy(self, pixmap):
        image = pixmap.toImage().convertToFormat(QImage.Format.Format_RGBA8888)
        bits = image.bits().asarray(image.byteCount())
        return np.frombuffer(bits, dtype=np.uint8).reshape(image.height(), image.width(), 4)

    def actualizar_imagen_filtrada(self):
        img_filtrada_pixmap = self.convertir_numpy_a_pixmap(self.img_filtrada)
        self.lbl_imagen_filtrada.setPixmap(img_filtrada_pixmap)

    def convertir_numpy_a_pixmap(self, img):
        height, width, channel = img.shape
        bytes_per_line = 4 * width
        q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format.Format_RGBA8888)
        return QPixmap.fromImage(q_image)
"""

app = QApplication([])
ventana = VentanaFiltroMediana()
ventana.show()
app.exec()
