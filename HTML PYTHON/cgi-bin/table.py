#!/usr/bin/env python3
import cgi
from random import *

#Создаем массив из 25 числел
dig = [x for x in range(25)]
#Перемешиваем их случайным образом
shuffle(dig)
#Выводим таблицу
print("Content-type: text/html\n")

print("""<!DOCTYPE HTML>
        <html>
        <head>           
                <title>Random Table of Digits</title>
        </head>
        <body>""")
print("""<table border = "1"><tr><td>""", z[0] ," </td><td>", z[1] ,"</td><td>", z[2] ," </td><td>", z[3] ," </td><td>", z[4] ," </td></tr>")
print("<tr><td>""", z[5] ," </td><td>", z[6] ,"</td><td>", z[7] ," </td><td>", z[8] ," </td><td>", z[9] ," </td></tr>")
print("<tr><td>""", z[10] ," </td><td>", z[11] ,"</td><td>", z[12] ," </td><td>", z[13] ," </td><td>", z[14] ," </td></tr>")
print("<tr><td>""", z[15] ," </td><td>", z[16] ,"</td><td>", z[17] ," </td><td>", z[18] ," </td><td>", z[19] ," </td></tr>")
print("<tr><td>""", z[20] ," </td><td>", z[21] ,"</td><td>", z[22] ," </td><td>", z[23] ," </td><td>", z[24] ," </td></tr></table>")


print("""</body>
        </html>""")
