import sys, os
from pathlib import Path

from datetime import datetime

import PySide2.QtWidgets as QT
from PySide2 import QtCore, QtGui

import pyexcel

class Egisso():
    def __init__(self):
        self._shablon = pyexcel.get_sheet(
            file_name=str(Path('shablon_3.xlsx')))
            
        self.itog_sheet = pyexcel.Sheet(name='Формат')
        self.itog_sheet.row += self._shablon

        self.path_to_excels = ''

        # временно
        self.list_of_file_names = []
        self.num_of_strokes = 0

        self.formLayout = QT.QFormLayout()
        self.group_box = QT.QGroupBox()
        self.group_box.setLayout(self.formLayout)

        #UI
        self.scroll = QT.QScrollArea()
        self.scroll.setWidget(self.group_box)
        self.scroll.setMinimumHeight(200)
        self.scroll.setWidgetResizable(True)
        self.scroll_layout = QT.QVBoxLayout()
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_layout.addWidget(self.scroll)
        
        self.update_scroll_list()

    def update_scroll_list(self):
        # очистка данных и отображения списка
        while self.formLayout.count():
            child = self.formLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # построение нового списка
        string_top = 'Всего ' + str(self.num_of_strokes) + ' строк' + ' в '+ str(len(self.list_of_file_names)) + ' файлах:'
        self.formLayout.addWidget(QT.QLabel(string_top))
        for name in self.list_of_file_names:
            wdgt = QT.QLabel(name)
            self.formLayout.addWidget(wdgt)

    def purge_data(self):
        self.itog_sheet = pyexcel.Sheet(name='Формат')
        self.itog_sheet.row += self._shablon

        self.path_to_excels = ''

        self.list_of_file_names = []
        self.num_of_strokes = 0

        self.update_scroll_list()

    def svod(self):
        """
        Складывает excel листы из выбранной директории (рекурсивно) в одну книгу
        """
        for f in Path(self.path_to_excels).rglob('*.xls*'):
            self.list_of_file_names.append(f.name)
            new_sheet = pyexcel.get_sheet(file_name=str(f), start_row=6)
            del new_sheet.row[filter_row]
            self.itog_sheet.row += new_sheet

        for i, row in enumerate(self.itog_sheet.rows()):
            if i < 6:
                continue
            self.num_of_strokes += 1
            row[0] = self.num_of_strokes

    def take_path_to_excels(self):
        # Очистка временных переменных
        self.num_of_strokes = 0

        self.path_to_excels = QT.QFileDialog().getExistingDirectory()
        self.svod()
        self.update_scroll_list()

# Глобальные переменные
app = QT.QApplication()
egisso = Egisso()


def filter_row(row_index, row):
    result = True if row[0] == '' else False
    return result

def save_egisso():
    formated_time = datetime.now().strftime('%Y%m%dT%H%M%S')
    egisso.itog_sheet.save_as('Загружено_'+ formated_time + '.xlsx')

    app.exit()

if __name__ == "__main__":
 

    container_layout = QT.QVBoxLayout()
    container = QT.QWidget()
    container.setLayout(container_layout)
    
    load_button = QT.QPushButton(text='load')
    load_button.clicked.connect(egisso.take_path_to_excels)
    
    clean_button = QT.QPushButton(text='clean')
    clean_button.clicked.connect(egisso.purge_data)

    save_button = QT.QPushButton(text='save and exit')
    save_button.clicked.connect(save_egisso)

    quit_button = QT.QPushButton(text='exit')
    quit_button.clicked.connect(app.exit)

    container_layout.addWidget(load_button)
    container_layout.addWidget(clean_button)
    container_layout.addWidget(egisso.scroll)
    container_layout.addWidget(save_button)
    container_layout.addWidget(quit_button)
    # container.resize(300, 600)
    container.setFixedSize(QtCore.QSize(300, 600))
    container.setWindowIcon(QtGui.QIcon('egisso.ico'))
    container.show()

    sys.exit(app.exec_())