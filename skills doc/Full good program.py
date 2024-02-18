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

data = good_football

result_good = [(data[i], data[i+1], data[i+2], data[i+3], data[i+4], data[i+5], data[i+6], data[i+7], data[i+8], data[i+9], data[i+10], data[i+11]) for i in range(0, len(data), 12)]


players = result_good

max_skills = 0
best_players = None
n = 15
# перебираем всех вратарей
for pos1 in range(n):
    # ЗП
    for pos2 in range(n):
        if pos1 == pos2:
            continue
        # ЗЦ
        for pos3 in range(n):
            if pos3 == pos1 or pos3 == pos2:
                continue
            # ЗЦ
            for pos4 in range(n):
                if pos4 == pos1 or pos4 == pos2 or pos4 == pos3:
                    continue
                # ЗЛ
                for pos5 in range(n):
                    if pos5 == pos1 or pos5 == pos2 or pos5 == pos3 or pos5 == pos4:
                        continue
                    #ПЦП
                    for pos6 in range(n):
                        if pos6 == pos1 or pos6 == pos2 or pos6 == pos3 or pos6 == pos4 or pos6 == pos5:
                            continue
                        #ПЦЛ
                        for pos7 in range(n):
                            if pos7 == pos1 or pos7 == pos2 or pos7 == pos3 or pos7 == pos4 or pos7 == pos5 or pos7 == pos6:
                                continue
                            # АПП
                            for pos8 in range(n):
                                if pos8 == pos1 or pos8 == pos2 or pos8 == pos3 or pos8 == pos4 or pos8 == pos5 or pos8 == pos6 or pos8 == pos7:
                                    continue
                                # АПЦ
                                for pos9 in range(n):
                                    if pos9 == pos1 or pos9 == pos2 or pos9 == pos3 or pos9 == pos4 or pos9 == pos5 or pos9 == pos6 or pos9 == pos7 or pos9 == pos8:
                                        continue
                                    # АПЛ
                                    for pos10 in range(n):
                                        if pos10 == pos1 or pos10 == pos2 or pos10 == pos3 or pos10 == pos4 or pos10 == pos5 or pos10 == pos6 or pos10 == pos7 or pos10 == pos8 or pos10 == pos9:
                                            continue
                                        # НПЦ
                                        for pos11 in range(n):
                                            if pos11 == pos1 or pos11 == pos2 or pos11 == pos3 or pos11 == pos4 or pos11 == pos5 or pos11 == pos6 or pos11 == pos7 or pos11 == pos8 or pos11 == pos9 or pos11 == pos10:
                                                continue
                                            skills = players[pos1][1] + players[pos2][2] + players[pos3][3] + players[pos4][4] + players[pos5][5] + players[pos6][6] + players[pos7][7] + players[pos8][8] + players[pos9][9] + players[pos10][10] + players[pos11][11]
                                            if skills > max_skills:
                                                max_skills = skills
                                                best_players = (players[1], players[2], players[3], players[4],players[5], players[6], players[7], players[8],players[9], players[10], players[11])

                                            data_new1 = max_skills
                                            data_new2 = players[1][0],players[2][0],players[3][0],players[4][0], players[5][0], players[6][0], players[7][0], players[8][0], players[9][0], players[10][0], players[11][0]

                                            with open("allfoot.txt", "a") as f:
                                                f.write(
                                                    "\n")  # добавляем пустую строку для отделения старых и новых данных
                                                f.write(f"{data_new1}   is {data_new2}")

print(f'Максимальная сумма навыков: {max_skills}')
print(f'Лучшие игроки: {best_players}')