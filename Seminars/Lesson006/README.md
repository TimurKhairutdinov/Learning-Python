1. Создайте программу для игры в "Крестики-нолики".

2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.


3. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 
    
    *Пример:* 
    
    2+2 => 4; 
    
    1+2*3 => 7; 
    
    1-2*3 => -5;
    
    - Добавьте возможность использования скобок, меняющих приоритет операций.
        
        *Пример:* 
        
        1+2*3 => 7; 
        
        (1+2)*3 => 9;

4. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

*Пример:* 

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]