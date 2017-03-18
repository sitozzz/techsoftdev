#!/usr/bin/env python3
import cgi
from random import *
def r():
        return randint(1,25)


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
           
            <title>Random Table of Digits</title>
        </head>
        <body>""")
print("""<table border = "1"><tr><td>""", r() ," </td><td>", r() ,"</td><td>", r() ," </td><td>", r() ," </td><td>", r() ," </td></tr>")
print("<tr><td>""", r() ," </td><td>", r() ,"</td><td>", r() ," </td><td>", r() ," </td><td>", r() ," </td></tr>")
print("<tr><td>""", r() ," </td><td>", r() ,"</td><td>", r() ," </td><td>", r() ," </td><td>", r() ," </td></tr>")
print("<tr><td>""", r() ," </td><td>", r() ,"</td><td>", r() ," </td><td>", r() ," </td><td>", r() ," </td></tr>")
print("<tr><td>""", r() ," </td><td>", r() ,"</td><td>", r() ," </td><td>", r() ," </td><td>", r() ," </td></tr></table>")


print("""</body>
        </html>""")
