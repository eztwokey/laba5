# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Даны два слова. 
  #  Для каждой буквы первого слова определить, входитли она во второе слово.
    one = 'Миграция'
    two = 'Народов'
    for i in one:
        print(i in two, end=' ')
