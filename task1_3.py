# Task 3
WORDS = ['attribute', 'класс', 'функция', 'type']

for i in WORDS:
    if not i.isascii():
        print(f'Слово "{i}" невозможно записать в байтовом типе')
