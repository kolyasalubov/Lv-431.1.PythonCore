a = float(input("Введіть а\n"))
b = float(input("Введіть b\n"))

try:
    d = a + b
    m = a - b
    mul = a * b
    dl = a / b
except ZeroDivisionError:
    print(f"Сума: {d} \nРізниця: {m} \nМноження: {mul}")
    print('Виявлено ділення на нуль, операцію завершено...')
else:
    print(f"Сума: {d} \nРізниця: {m} \nМноження: {mul} \nДілення: {dl}")