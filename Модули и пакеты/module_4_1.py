from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Примеры вызовов функций
result1 = fake_divide(69, 3)  # Ожидается 23.0
result2 = fake_divide(3, 0)    # Ожидается 'Ошибка'
result3 = true_divide(49, 7)   # Ожидается 7.0
result4 = true_divide(15, 0)   # Ожидается inf

# Вывод результатов
print(result1)
print(result2)
print(result3)
print(result4)