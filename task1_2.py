# Task 2
words = ['class', 'function', 'method']

for i in words:
    el = eval(f"b'{i}'")
    print('=' * 30)
    print(type(el), el, len(el))
