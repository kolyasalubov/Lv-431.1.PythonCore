name = input('What is ur name?\n')
if not name.isalpha():
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
        if not place.isalpha():
            print('Назва міста не може містити циферки...')
            quit()
        else:
            print(f"Hello, {name} :) \nUr age is {age}. \nU live in {place}.")