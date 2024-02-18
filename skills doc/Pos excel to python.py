# Программа изменяет значение из excel в python
# =C65+D65+E65+F65+G65+H65+I65+J65+K65+L65+M65+N65+O65+P65+Q65+R65+S65+T65+U65+V65+W65+X65+Y65+Z65+AA65+AB65+AC65+AD65+AE65+AF65+AG65+AH65+AI65+AJ65+AK65+AL65+AM65+AN65+AO65+AP65+AQ65+AR65+AS65+AT65+AU65+AV65+AW65
i = "AA2+AD2+AF2+AG2+AK2+AN2+AO2+AU2+AV2"
i = i.replace("2","")
list_i = i.split("+")
print(len(list_i))
d = ["ZERO","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK","AL","AM","AN","AO","AP","AQ","AR","AS","AT","AU","AV","AW"]
i_good = str()
number = 0
for item in d:
    if item in list_i:
        i_good += f"int(values[{str(number)}])+"
    number += 1
print(f"round(({i_good[0:-1]}) / {len(list_i)}, 2)")