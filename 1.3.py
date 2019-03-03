temp = input()
if temp[0] in ['c', 'C']:
    F = eval(temp[1:])*1.8+32
    print("F{:.2f}".format(F))
elif temp[0] in ['F', 'f']:
    C = (eval(temp[1:])-32)/1.8  # -*- coding: utf-8 -*-
    print("C{:0.2f}".format(C))
