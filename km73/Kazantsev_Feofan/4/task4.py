Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> q = int(input())
if (q % 4 == 0 and q % 100 != 0) or q % 400 == 0 :
    answer="LEAP"
else :
    answer="СOMMON"
print (answer)
