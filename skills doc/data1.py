data = [' Григорий Юдин ', 3.95, 5.94, 5.65, 5.65, 5.94, 5.73, 6.65, 6.07, 6.31, 6.21, 7.29, ' Tiarnan Boorman ', 4.21, 5.89, 6.35, 6.35, 5.89, 5.64, 6.3, 5.87, 6.25, 6.14, 7.41]

result = [(data[i], data[i+1], data[i+2], data[i+3], data[i+4], data[i+5], data[i+6], data[i+7], data[i+8], data[i+9], data[i+10], data[i+11])
          for i in range(0, len(data), 12)]

print(result)