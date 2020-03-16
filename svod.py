import sys, os
from pathlib import Path

from datetime import datetime

import PySide2.QtWidgets as QT
from PySide2 import QtCore, QtGui

import pyexcel
import pyexcel_xls
import pyexcel_xlsx

# import count_facts.count_facts

class Egisso():
    def __init__(self):
        self.shablon = pyexcel.get_sheet(
            file_name=str(Path('./data/shablon_3.xlsx')))
            
        self.itog_sheet = pyexcel.Sheet(name='Формат')
        self.itog_scolls_sheet = pyexcel.Sheet(name='Формат')
        self.itog_sady_sheet = pyexcel.Sheet(name='Формат')

        self.total_count = 0
        self.total_scolls_count = 0
        self.total_sady_count = 0

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
        string_top = 'Всего ' + str(self.num_of_strokes) + ' строк' + ' в '+ str(self.total_count) + ' файлах:'
        self.formLayout.addWidget(QT.QLabel(string_top))
        for name in self.list_of_file_names:
            wdgt = QT.QLabel(name)
            self.formLayout.addWidget(wdgt)

    def purge_data(self):
        self.itog_sheet = pyexcel.Sheet(name='Формат')
        self.itog_scolls_sheet = pyexcel.Sheet(name='Формат')
        self.itog_sady_sheet = pyexcel.Sheet(name='Формат')

        self.total_count = 0
        self.total_scolls_count = 0
        self.total_sady_count = 0

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
            new_sheet = pyexcel.Sheet()
            print(f)
            new_sheet = pyexcel.get_sheet(file_name=str(f), start_row=6)
            # except:
            #     print(f)
            del new_sheet.row[filter_row]
            self.itog_sheet.row += new_sheet

            self.total_count += 1
            if 'СОШ' in f.stem.upper():
                self.itog_scolls_sheet.row += new_sheet
                self.total_scolls_count += 1
            if 'САД' in f.stem.upper():
                self.itog_sady_sheet.row += new_sheet
                self.total_sady_count += 1

        for i, row in enumerate(self.itog_sheet.rows()):
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

name_for_uuid = {
    'd90b5df8-54b2-4a88-9302-fe35c3a08f44': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (педагоги)',
    'cef59820-c062-489b-a43e-7eca1089a5be': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (пенсионеры)',
    'dbbbeafb-590b-4bdf-97a2-569a8afe6d7f': 
        'Компенсация части платы взимаемой с родителей',
    '4b120a4b-b68c-436d-a24d-fc62683e46bb': 
        'Полное или частичное освобождение от родительской платы за присмотр и уход за ребенком, осваивающим образовательную программу дошкольного образования в организации, осуществляющей образовательную деятельность (содержание ребенка в дошкольной образовательной организации)',
    '17f046ea-a5e5-49b3-a75a-b13f832bea2b': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (и пенсионеры, и педагоги, деления нет)',
    '6f712658-3040-4402-82c8-a71eddf15513': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (педагоги)',
    'ccf49282-8cb1-4fd1-93a3-4acff183bcd8': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (пенсионеры)',
    'df7a014d-a8bc-411d-b103-ad105d94f24e': 
        'Предоставление бесплатного питания',
    'ea4ca0d2-65eb-4b9b-980a-7a804ab40731': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (и пенсионеры, и педагоги, деления нет)',
    '5c64e81d-db3b-4f00-8c22-681e48d1d329': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (и пенсионеры, и педагоги, деления нет)',
    '324d6e47-f1f0-478e-83ee-aeb40c3817dd': 
        'Выплата на содержание детей-сирот и детей, оставшихся без попечения родителей в семье опекуна, приемной семье',
    '36c2a946-0bb7-4b1a-a2bf-d947b6f1019c': 
        'Выплата на содержание детей-сирот и детей, оставшихся без попечения родителей в семье опекуна, приемной семье',
    '34a0ac95-a8db-4a94-bc27-8e2eff70db25': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (35)',
    '7c48ccc0-d936-4043-83af-1fd039ca1049': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (31)',
    '4630ba88-0367-4c64-9bc9-4b721055b502': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (34)',
    '7c89a01d-b4ce-4b10-bb01-44e9abde230d': 
        'Возмещение расходов по оплате жилого помещения, отопления и освещения (30)'
}

name_for_compose_uuid = {
    'Возмещение расходов по оплате жилого помещения':
        [
        'd90b5df8-54b2-4a88-9302-fe35c3a08f44',
        'cef59820-c062-489b-a43e-7eca1089a5be',
        '17f046ea-a5e5-49b3-a75a-b13f832bea2b',
        '6f712658-3040-4402-82c8-a71eddf15513',
        'ccf49282-8cb1-4fd1-93a3-4acff183bcd8',
        'ea4ca0d2-65eb-4b9b-980a-7a804ab40731',
        '5c64e81d-db3b-4f00-8c22-681e48d1d329',
        '34a0ac95-a8db-4a94-bc27-8e2eff70db25',
        '7c48ccc0-d936-4043-83af-1fd039ca1049',
        '4630ba88-0367-4c64-9bc9-4b721055b502',
        '7c89a01d-b4ce-4b10-bb01-44e9abde230d'],
    'Компенсация части платы взимаемой с родителей':
        [
            'dbbbeafb-590b-4bdf-97a2-569a8afe6d7f'
        ],
    'Полное или частичное освобождение от родительской платы за присмотр и уход за ребенком, осваивающим образовательную программу дошкольного образования в организации, осуществляющей образовательную деятельность (содержание ребенка в дошкольной образовательной организации)':
        [
            '4b120a4b-b68c-436d-a24d-fc62683e46bb'
        ],
    'Предоставление бесплатного питания':
        [
            'df7a014d-a8bc-411d-b103-ad105d94f24e'
        ],
    'Выплата на содержание детей-сирот и детей, оставшихся без попечения родителей в семье опекуна, приемной семье':
        [
            '324d6e47-f1f0-478e-83ee-aeb40c3817dd',
            '36c2a946-0bb7-4b1a-a2bf-d947b6f1019c'
        ]
}

def to_number(input_str:str=''):
    out = 0
    if type(input_str) == str:
        input_str = input_str.replace(',','.')
    if input_str != '':
        out = float(input_str)
    return out

def filter_row(row_index, row):
    #TODO: Сделать более честную фильтрацию
    result = True if row[0] == '' else False
    return result

def save_egisso():
    sheet_to_save = pyexcel.Sheet(name='Формат')
    sheet_to_save.row += egisso.shablon
    sheet_to_save.row += egisso.itog_sheet

    formated_time = datetime.now().strftime('%Y%m%dT%H%M%S')
    sheet_to_save.save_as('Загружено_' + formated_time + '.xlsx')

    app.exit()

def report_mera_uuid(input_sheet):

    # egisso.itog_sheet[6,30] # Код МСЗ (31 столбец)
    # egisso.itog_sheet[6,37] # Начисление МСЗ (38 столбец)

    list_of_column_50 = ['df7a014d-a8bc-411d-b103-ad105d94f24e',
                        '4b120a4b-b68c-436d-a24d-fc62683e46bb']

    out_dict = {}
    out_dict.setdefault('',[0,0])

    for i, row in enumerate(input_sheet.rows()):
        uuid = row[30]
        if uuid not in out_dict:
            out_dict[uuid] = [1, 0]
            if uuid in list_of_column_50:
                out_dict[uuid][1] += to_number(row[49])
            else:
                out_dict[uuid][1] += to_number(row[37])
        else:
            out_dict[uuid][0] += 1
            if uuid in list_of_column_50:
                out_dict[uuid][1] += to_number(row[49])
            else:
                out_dict[uuid][1] += to_number(row[37])

    
    return out_dict

def report_mera_name_of_uuid(meras_raw_dict):
    meras_dict_compose = {}
    meras_dict_compose.setdefault('',[0,0])
    del meras_dict_compose['']

    for mera_uuid in meras_raw_dict:
        for compose_key in name_for_compose_uuid:
            if mera_uuid in name_for_compose_uuid[compose_key]:
                if compose_key not in meras_dict_compose:
                    meras_dict_compose[compose_key] = [0,0]
                    meras_dict_compose[compose_key][0] = meras_raw_dict[mera_uuid][0]
                    meras_dict_compose[compose_key][1] = meras_raw_dict[mera_uuid][1]
                else:
                    meras_dict_compose[compose_key][0] += meras_raw_dict[mera_uuid][0]
                    meras_dict_compose[compose_key][1] += meras_raw_dict[mera_uuid][1]
    return meras_dict_compose

def report():
    report_sheet = pyexcel.Sheet(name='report')
    report_sheet.row += ['Мера', 'Количество', 'Сумма']

    report_sheet.row += ['ШКОЛЫ', egisso.total_scolls_count]
    meras_raw_dict = report_mera_uuid(egisso.itog_scolls_sheet)

    meras_dict_compose = report_mera_name_of_uuid(meras_raw_dict)

    for mera_uuid in meras_dict_compose:
        report_sheet.row += [mera_uuid,
                            meras_dict_compose[mera_uuid][0],
                            meras_dict_compose[mera_uuid][1]]

    report_sheet.row += ['Сады', egisso.total_sady_count]
    meras_raw_dict = report_mera_uuid(egisso.itog_sady_sheet)

    meras_dict_compose = report_mera_name_of_uuid(meras_raw_dict)
    
    for mera_uuid in meras_dict_compose:
        report_sheet.row += [mera_uuid,
                            meras_dict_compose[mera_uuid][0],
                            meras_dict_compose[mera_uuid][1]]

    report_sheet.row += ['ВСЕГО', egisso.total_count]
    meras_raw_dict = report_mera_uuid(egisso.itog_sheet)

    meras_dict_compose = report_mera_name_of_uuid(meras_raw_dict)
    
    for mera_uuid in meras_dict_compose:
        report_sheet.row += [mera_uuid,
                            meras_dict_compose[mera_uuid][0],
                            meras_dict_compose[mera_uuid][1]]


    formated_time = datetime.now().strftime('%Y%m%dT%H%M%S')
    report_sheet.save_as('Отчёт_' + formated_time + '.xlsx')

if __name__ == "__main__":
    container_layout = QT.QVBoxLayout()
    container = QT.QWidget()
    container.setLayout(container_layout)
    
    load_button = QT.QPushButton(text='load')
    load_button.clicked.connect(egisso.take_path_to_excels)
    
    clean_button = QT.QPushButton(text='clean')
    clean_button.clicked.connect(egisso.purge_data)

    report_button = QT.QPushButton(text='report (amount | sum)')
    report_button.clicked.connect(report)

    save_button = QT.QPushButton(text='save and exit')
    save_button.clicked.connect(save_egisso)

    quit_button = QT.QPushButton(text='exit')
    quit_button.clicked.connect(app.exit)

    container_layout.addWidget(load_button)
    container_layout.addWidget(clean_button)
    container_layout.addWidget(egisso.scroll)
    container_layout.addWidget(report_button)
    container_layout.addWidget(save_button)
    container_layout.addWidget(quit_button)
    # container.resize(300, 600)
    container.setFixedSize(QtCore.QSize(300, 600))
    container.setWindowIcon(QtGui.QIcon('data\\egisso.ico'))
    container.setWindowTitle('Egisso')
    container.show()

    sys.exit(app.exec_())