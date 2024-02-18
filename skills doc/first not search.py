from lxml import etree
import re

HtmlFile = open("year20.html", 'r', encoding='utf-8')  # мы берем данные из таблицы year20.html
s = HtmlFile.read()  # мы берем данные из таблицы

good_values = []  # итоговое сюда, без изменения способности
good_football = []  # итоговое f для football

table = etree.HTML(s).find("body/table")
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]

    pos_1_g = round((int(values[5]) + int(values[8]) + int(values[10]) + int(values[18]) + int(values[29]) + int(
        values[32]) + int(values[34]) + int(values[44])) / 8, 2)
    pos_1_f = round((int(values[3]) + int(values[4]) + int(values[5]) + int(values[6]) + int(values[7]) + int(
        values[8]) + int(values[10]) + int(values[11]) + int(values[18]) + int(values[22]) + int(values[24]) + int(
        values[28]) + int(values[29]) + int(values[32]) + int(values[34]) + int(values[36]) + int(values[39]) + int(
        values[44]) + int(values[48])) / 19, 2)
    pos_2_g = round((int(values[15]) + int(values[19]) + int(values[20]) + int(values[21]) + int(values[30]) + int(
        values[33]) + int(values[37]) + int(values[41]) + int(values[48])) / 9, 2)
    pos_2_f = round((int(values[15]) + int(values[19]) + int(values[20]) + int(values[21]) + int(values[22]) + int(
        values[24]) + int(values[25]) + int(values[29]) + int(values[30]) + int(values[32]) + int(values[33]) + int(
        values[34]) + int(values[36]) + int(values[37]) + int(values[41]) + int(values[44]) + int(values[47]) + int(
        values[48])) / 18, 2)
    pos_3_g = round((int(values[17]) + int(values[20]) + int(values[21]) + int(values[22]) + int(values[29]) + int(
        values[39]) + int(values[42]) + int(values[46])) / 8, 2)
    pos_3_f = round((int(values[17]) + int(values[20]) + int(values[21]) + int(values[22]) + int(values[24]) + int(
        values[25]) + int(values[27]) + int(values[28]) + int(values[29]) + int(values[32]) + int(values[34]) + int(
        values[36]) + int(values[39]) + int(values[40]) + int(values[42]) + int(values[46]) + int(values[47])) / 17, 2)
    pos_4_g = round((int(values[17]) + int(values[20]) + int(values[21]) + int(values[22]) + int(values[29]) + int(
        values[39]) + int(values[42]) + int(values[46])) / 8, 2)
    pos_4_f = round((int(values[17]) + int(values[20]) + int(values[21]) + int(values[22]) + int(values[24]) + int(
        values[25]) + int(values[27]) + int(values[28]) + int(values[29]) + int(values[32]) + int(values[34]) + int(
        values[36]) + int(values[39]) + int(values[40]) + int(values[42]) + int(values[46]) + int(values[47])) / 17, 2)
    pos_5_g = round((int(values[20]) + int(values[21]) + int(values[29]) + int(values[32]) + int(values[33]) + int(
        values[37]) + int(values[41]) + int(values[48])) / 8, 2)
    pos_5_f = round((int(values[15]) + int(values[19]) + int(values[20]) + int(values[21]) + int(values[22]) + int(
        values[24]) + int(values[25]) + int(values[29]) + int(values[30]) + int(values[32]) + int(values[33]) + int(
        values[34]) + int(values[36]) + int(values[37]) + int(values[41]) + int(values[44]) + int(values[47]) + int(
        values[48])) / 18, 2)
    pos_6_g = round((int(values[22]) + int(values[24]) + int(values[25]) + int(values[28]) + int(values[33]) + int(
        values[36]) + int(values[39])) / 7, 2)
    pos_6_f = round((int(values[22]) + int(values[24]) + int(values[25]) + int(values[28]) + int(values[29]) + int(
        values[30]) + int(values[32]) + int(values[33]) + int(values[36]) + int(values[39]) + int(values[43])) / 11, 2)
    pos_7_g = round(
        (int(values[21]) + int(values[22]) + int(values[30]) + int(values[33]) + int(values[37]) + int(values[41])) / 6,
        2)
    pos_7_f = round((int(values[14]) + int(values[15]) + int(values[16]) + int(values[21]) + int(values[22]) + int(
        values[24]) + int(values[25]) + int(values[27]) + int(values[29]) + int(values[30]) + int(values[32]) + int(
        values[33]) + int(values[36]) + int(values[37]) + int(values[39]) + int(values[41]) + int(values[43]) + int(
        values[46]) + int(values[47]) + int(values[48])) / 20, 2)
    pos_8_g = round(
        (int(values[15]) + int(values[22]) + int(values[25]) + int(values[30]) + int(values[44]) + int(values[48])) / 6,
        2)
    pos_8_f = round((int(values[14]) + int(values[15]) + int(values[19]) + int(values[22]) + int(values[24]) + int(
        values[25]) + int(values[28]) + int(values[30]) + int(values[31]) + int(values[32]) + int(values[36]) + int(
        values[39]) + int(values[44]) + int(values[47]) + int(values[48])) / 15, 2)
    pos_9_g = round((int(values[15]) + int(values[16]) + int(values[24]) + int(values[30]) + int(values[32]) + int(
        values[39]) + int(values[48])) / 7, 2)
    pos_9_f = round((int(values[15]) + int(values[16]) + int(values[22]) + int(values[24]) + int(values[25]) + int(
        values[30]) + int(values[32]) + int(values[34]) + int(values[36]) + int(values[37]) + int(values[39]) + int(
        values[41]) + int(values[43]) + int(values[44]) + int(values[47]) + int(values[48])) / 16, 2)
    pos_10_g = round((int(values[15]) + int(values[16]) + int(values[24]) + int(values[25]) + int(values[30]) + int(
        values[43]) + int(values[44]) + int(values[48])) / 8, 2)
    pos_10_f = round((int(values[14]) + int(values[15]) + int(values[16]) + int(values[22]) + int(values[24]) + int(
        values[25]) + int(values[30]) + int(values[31]) + int(values[32]) + int(values[39]) + int(values[43]) + int(
        values[44]) + int(values[47]) + int(values[48])) / 14, 2)
    pos_11_g = round((int(values[27]) + int(values[30]) + int(values[32]) + int(values[33]) + int(values[37]) + int(
        values[40]) + int(values[41]) + int(values[47]) + int(values[48])) / 9, 2)
    pos_11_f = round((int(values[16]) + int(values[24]) + int(values[27]) + int(values[30]) + int(values[32]) + int(
        values[33]) + int(values[34]) + int(values[36]) + int(values[37]) + int(values[39]) + int(values[40]) + int(
        values[41]) + int(values[43]) + int(values[44]) + int(values[46]) + int(values[47]) + int(values[48])) / 17, 2)

    # пошло добро с В / ЗП / ЗЦ / ЗЦ / ЗЛ / ПЦП / ПЦЛ / АПП / АПЦ / АПЛ / НПЦ
    values[0] = re.sub(r'\([^)]*\)', '', values[0])
    good_football.append(f"{values[0]}")
    good_values.append(f"(В+){values[0]}({(pos_1_g)})")
    good_values.append(f"(В%){values[0]}({(pos_1_f)})")
    good_football.append(pos_1_f)
    good_values.append(f"(ЗП+){values[0]}({(pos_2_g)})")
    good_values.append(f"(ЗП%){values[0]}({(pos_2_f)})")
    good_football.append(pos_2_f)
    good_values.append(f"(ЗЦ+){values[0]}({(pos_3_g)})")
    good_values.append(f"(ЗЦ%){values[0]}({(pos_3_f)})")
    good_football.append(pos_3_f)
    good_values.append(f"(ЗЦ+){values[0]}({(pos_4_g)})")
    good_values.append(f"(ЗЦ%){values[0]}({(pos_4_f)})")
    good_football.append(pos_4_f)
    good_values.append(f"(ЗЛ+){values[0]}({(pos_5_g)})")
    good_values.append(f"(ЗЛ%){values[0]}({(pos_5_f)})")
    good_football.append(pos_5_f)
    good_values.append(f"(ПЦП+){values[0]}({(pos_6_g)})")
    good_values.append(f"(ПЦП%){values[0]}({(pos_6_f)})")
    good_football.append(pos_6_f)
    good_values.append(f"(ПЦЛ+){values[0]}({(pos_7_g)})")
    good_values.append(f"(ПЦЛ%){values[0]}({(pos_7_f)})")
    good_football.append(pos_7_f)
    good_values.append(f"(АПП+){values[0]}({(pos_8_g)})")
    good_values.append(f"(АПП%){values[0]}({(pos_8_f)})")
    good_football.append(pos_8_f)
    good_values.append(f"(АПЦ+){values[0]}({(pos_9_g)})")
    good_values.append(f"(АПЦ%){values[0]}({(pos_9_f)})")
    good_football.append(pos_9_f)
    good_values.append(f"(АПЛ+){values[0]}({(pos_10_g)})")
    good_values.append(f"(АПЛ%){values[0]}({(pos_10_f)})")
    good_football.append(pos_10_f)
    good_values.append(f"(НПЦ+){values[0]}({(pos_11_g)})")
    good_values.append(f"(НПЦ%){values[0]}({(pos_11_f)})")
    good_football.append(pos_11_f)

print(good_values)
print(good_football)

