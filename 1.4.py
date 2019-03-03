hb = input()
if hb[0:3] in ['RMB']:
    USD = eval(hb[3:])/6.78
    print("USD{:.2f}".format(USD))
elif hb[0:3] in ['USD']:
    RMB = eval(hb[3:])*6.78
    print("RMB{:.2f}".format(RMB))
