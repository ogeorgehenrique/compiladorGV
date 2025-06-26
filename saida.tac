func main
a = 2
b = 2
_t0 = a > b
if _t0 goto L0
goto L1
L0:
param "A maior"
call escreva
goto L2
L1:
param "B maior"
call escreva
L2:
return 0
endfunc
