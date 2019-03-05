daydayup1 = 1
for i in range(365):
    daydayup1 = daydayup1*(1+0.01)
print("{:.3f}".format(daydayup1))


def dayUP(df):
    daydayup = 1.0
    for i in range(365):
        if i % 7 in [0, 6]:
            daydayup = daydayup*(1-0.01)
        else:
            daydayup = daydayup*(1+df)
    return daydayup


up = 0.01
while dayUP(up) < daydayup1:
    up = up+0.0001
print("目标值为{:.4f}".format(up))
