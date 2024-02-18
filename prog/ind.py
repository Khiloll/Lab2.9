#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Опишите рекурсивную функцию, которая по заданным вещественному х и целому n
# вычисляет величину x^n.

def check_brackets(string, idx=0, open_brackets=0):
    # Базовый случай: достигнут конец строки
    if idx == len(string):
        # Если все скобки сбалансированы, количество открывающих и закрывающих скобок равно
        return open_brackets == 0
    # Если открывающая скобка, увеличиваем счетчик открытых скобок
    if string[idx] == '(':
        return check_brackets(string, idx + 1, open_brackets + 1)
    # Если закрывающая скобка, уменьшаем счетчик открытых скобок
    elif string[idx] == ')':
        # Если закрывающей скобки не может быть без соответствующей открывающей
        if open_brackets == 0:
            return False
        return check_brackets(string, idx + 1, open_brackets - 1)
    # Пропускаем другие символы
    return check_brackets(string, idx + 1, open_brackets)

# Примеры использования
print(check_brackets("((()))"))
print(check_brackets("(()))"))
print(check_brackets("())("))
