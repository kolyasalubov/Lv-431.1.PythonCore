try:
    a = float(input("Введіть число а\n"))
    b = float(input("Введіть число b\n"))
    d = a + b
    m = a - b
    mul = a * b
    dl = a / b
except ZeroDivisionError:
    print(f"Сума: {d} \nРізниця: {m} \nМноження: {mul}")
    print('Виявлено ділення на нуль, операцію завершено...')
except ValueError:
    print("Ми тут працюємо з циферками...")
except:
    print("Ой, щось пішло не так...")
else:
    print(f"Сума: {d} \nРізниця: {m} \nМноження: {mul} \nДілення: {dl}")