# 1. Напишите программу вычисления арифметического выражения заданного
#  строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
#     *Пример:* 
#     2+2 => 4; 
#     1+2*3 => 7; 
#     1-2*3 => -5;
#      - Добавьте возможность использования скобок, меняющих 
#      приоритет операций.
#         Пример:* 
#       1+2*3 => 7; 
#      (1+2)*3 => 9;

import re
import copy

calculator = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
}
first = ('*', '/')
second = ('+', '-')

def calc_numbers (first_number, simbol, second_number):
        ex = calculator[simbol](first_number,second_number)
        return ex

def math (expression, simbol):
    numbers = re.findall(r'\d+', expression)

    i=0
    k=0
    while i < len(numbers)-1:
        num = expression.find(numbers[i], k)
        kol = len(numbers[i])
        j = expression[num+kol]
        k = num + kol # определение с какого индекса нужно искать значение, чтобы одинаковые цифры не задублились.
        if j in simbol:
            c = calc_numbers(int(numbers[i]), j , int(numbers[i+1]))
            expression = expression.replace(str(numbers[i]) + j + str(numbers[i+1]), str(c))
            numbers.pop(i)
            numbers[i]=str(c)
            k = k - kol
        else: 
            i +=1
    return expression


def open_brackets(expression, poz = 0):
    new_str = '' 
    if expression.find('(', poz) == -1:
        return chose_simbol(expression)
    else:
        j = expression.find('(', poz) + 1
        while expression[j] != ')':
            if expression[j] == '(':
                return open_brackets(expression, j )
            else:
                new_str += expression[j]
                j +=1
        s = chose_simbol(new_str)
        expression = expression.replace('('+ new_str + ')', s)
        return open_brackets(expression[:])

def chose_simbol (expression):
    for i in first:
        if i in expression:
            expression = math(expression, first)
    for i in second:
        if i in expression:
            expression = math(expression, second)
    
    return expression

some_str = '((6*(3+5)+1)*3)*(5-2)'
f = copy.deepcopy(some_str)
some_str = open_brackets(some_str)
print (f'{f} = {some_str}')
