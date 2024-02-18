from pyRTF import *

# Открываем документ RTF
rtf_file = RtfDocument()
rtf_file.read('new22.rtf')

# Извлекаем данные из таблицы
data_list = []

# Итерируемся по элементам документа
for elem in rtf_file.content:
    if isinstance(elem, RtfTable):
        for row in elem.rows:
            if len(row.cells) >= 2:
                name = row.cells[0].content.strip()
                input_value = row.cells[1].content.strip()
                data_list.append((name, input_value))

# Выводим полученные данные
for item in data_list:
    print(f'Имя: {item[0]}, Ввод: {item[1]}')

         # литера f - обозначает фулл статы
         # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
pos_1_f = [0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]
pos_1_g = [0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0]
         # 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
pos_2_f =
pos_2_g =