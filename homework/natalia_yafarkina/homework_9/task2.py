temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
hot_temperatures = list(filter(lambda x: x > 28, temperatures))
avg_hot_temperatures = (sum(hot_temperatures) / len(hot_temperatures))
max_hot_temperatures = max(hot_temperatures)
min_hot_temperatures = min(hot_temperatures)
print('температура выше 28 за период наблюдений: ', hot_temperatures)
print('максимальная температура за период наблюдений: ', max_hot_temperatures)
print('минимальная температура за период наблюдений: ', min_hot_temperatures)
print('средняя температура за период наблюдений: ', avg_hot_temperatures)
