func main
a = 3
b = 4
c = 5
_t0 = a + b
_t1 = _t0 > c
_t2 = a + c
_t3 = _t2 > b
_t4 = _t1 && _t3
_t5 = b + c
_t6 = _t5 > a
_t7 = _t4 && _t6
if _t7 goto L0
goto L1
L0:
_t8 = a == b
_t9 = b == c
_t10 = _t8 && _t9
if _t10 goto L3
goto L4
L3:
print "Triangulo Equilatero"
goto L5
L4:
L5:
_t11 = a == b
_t12 = a == c
_t13 = _t11 || _t12
_t14 = b == c
_t15 = _t13 || _t14
if _t15 goto L6
goto L7
L6:
print "Triangulo Isosceles"
goto L8
L7:
print "Trinagulo Escaleno"
L8:
goto L2
L1:
print "Nao forma triangulo"
L2:
return 0
endfunc
