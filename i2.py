import sys


if __name__ == '__main__':
# Даны два слова. 
# Определить, сколько начальных букв первого слова совпадает сначальными буквами второго слова.
 def fun(a, b):
    res = 0
    for x, y in zip(a, b):
        if x != y:
            break
        res += 1
    return res
print(fun('Катастрофа', 'Катастрофа'))
