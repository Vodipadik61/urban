#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(2, 2, 2)
print_params("hello")
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:
values_list = [1, "str", False]
values_dict = {'a' : "char", 'b' : False, 'c' : 25 }

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = ['e', 2.2]

print_params(*values_list_2, 42)
