# Task 6
from chardet import detect

WORDS = ['сетевое программирование', 'сокет', 'декоратор']
with open('test_file.txt', 'w') as file:
    for strs in WORDS:
        file.write(f'{strs}\n')
file.close()

with open('test_file.txt', 'rb') as file:
    coding = detect(file.read())['encoding']
    file.seek(0)
    print(file.read().decode(coding))
