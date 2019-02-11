"C:\Users\walterka\PycharmProjects\Python cursus\venv\Scripts\python.exe" "C:\Program Files\JetBrains\PyCharm 2018.3.4\helpers\pydev\pydevconsole.py" --mode=client --port=64301

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\walterka\\PycharmProjects\\Python cursus', 'C:/Users/walterka/PycharmProjects/Python cursus'])

PyDev console: starting.

Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
>>> grades = [9,7,7,10,3,9,6,6,2]
>>> grades.count(7)
2
>>> grades[8]= 4
>>> grades
[9, 7, 7, 10, 3, 9, 6, 6, 4]
>>> max(grades)
10
>>> grades.sort()
>>> grades
[3, 4, 6, 6, 7, 7, 9, 9, 10]
>>> sum(grades)/9
6.777777777777778