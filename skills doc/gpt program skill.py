players = [
    ('Иван', 80, 70, 50, 90),
    ('Петр', 70, 80, 60, 70),
    ('Сергей', 60, 80, 70, 80),
    ('Алексей', 90, 60, 50, 70),
    ('Максим', 60, 70, 80, 60),
    ('Дмитрий', 80, 50, 70, 80),
    ('Андрей', 70, 70, 60, 90),
    ('Николай', 50, 80, 70, 60),
    ('Константин', 70, 60, 80, 50),
    ('Артем', 80, 50, 70, 70)
]

max_skills = 0
best_players = None

# перебираем всех вратарей
for gk in range(10):
    # перебираем всех защитников
    for df in range(10):
        if df == gk:
            continue
        # перебираем всех полузащитников
        for mf in range(10):
            if mf == gk or mf == df:
                continue
            # перебираем всех нападающих
            for fw in range(10):
                if fw == gk or fw == df or fw == mf:
                    continue
                # считаем сумму навыков и сохраняем ее, если она больше предыдущих
                skills = players[gk][1] + players[df][2] + players[mf][3] + players[fw][4]
                if skills > max_skills:
                    max_skills = skills
                    best_players = (players[gk], players[df], players[mf], players[fw])

print(f'Максимальная сумма навыков: {max_skills}')
print(f'Лучшие игроки: {best_players}')