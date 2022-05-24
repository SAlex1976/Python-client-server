# Task 4
WORDS = ['разработка', 'администрирование', 'protocol', 'standard']
BYTES_WORD = []

for i in WORDS:
    bts = i.encode('utf-8')
    BYTES_WORD.append(bts)
    print(i, '=', bts)

for i in BYTES_WORD:
    bts = i.decode('utf-8')
    print(i, '=', bts)
