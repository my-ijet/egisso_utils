import os
from pathlib import Path

from datetime import datetime

import PySide2.QtWidgets as QT

import pyexcel

def filter_row(row_index, row):
    result = True if row[0] == '' else False
    return result

def svod(path_to_excels):
    """
    Складывает excel листы из выбранной директории (рекурсивно) в одну книгу
    """
    msgbox = QT.QMessageBox()

    shablon = pyexcel.get_sheet(file_name=str(Path('shablon_3.xlsx')))

    itog_sheet = pyexcel.Sheet(name='Формат')
    itog_sheet.row += shablon

    list_of_file_names = []
    for f in Path(path_to_excels).rglob('*.xls*'):
        list_of_file_names.append(f.name)
        new_sheet = pyexcel.get_sheet(file_name=str(f), start_row=6)
        del new_sheet.row[filter_row]
        itog_sheet.row += new_sheet

    num_of_strokes = 0
    for i, row in enumerate(itog_sheet.rows()):
        if i < 6:
            continue
        num_of_strokes += 1
        row[0] = num_of_strokes

    formated_time = datetime.now().strftime('%Y%m%dT%H%M%S')
    itog_sheet.save_as('Загружено_'+ formated_time + '.xlsx')

    string_top = 'Всего ' + str(num_of_strokes) + ' строк\n' + 'В файлах:\n'
    print(list_of_file_names)
    for name in list_of_file_names:
        string_top += name + '\n'
    msgbox.setText(string_top)
    msgbox.exec()

if __name__ == "__main__":
    app = QT.QApplication()
    source_dir = QT.QFileDialog().getExistingDirectory()

    if source_dir !='':
        svod(source_dir)