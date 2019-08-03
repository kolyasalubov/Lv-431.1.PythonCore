def name_place_test(obj):
    numb_count = 0
    for i in obj:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            numb_count += 1
    if numb_count > 0:
        return False
    return True


name = input('What is ur name?\n')
if not name_place_test(name):
    print('Ім\'я не може містити циферки...')
    quit()
else:
    try:
        age = int(input('How old are u?\n'))
    except ValueError:
        print('Вік потрібно вказати цифрами!')
        quit()
    else:
        place = input('Where do u live?\n')
        if not name_place_test(place):
            print('Назва міста не може містити циферки...')
            quit()
        else:
            print(f"Hello, {name} :) \nUr age is {age}. \nU live in {place}.")