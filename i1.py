# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
# Дано слово. Добавить к нему в начале и конце столько звездочек, сколько букв в этом слове.
    s = input()
    print('*'*len(s)+s+('*'*len(s)))
