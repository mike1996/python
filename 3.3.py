# daydayupQ3
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup*(1)
    else:
        dayup = dayup*(1+dayfactor)
print("dayup:{:0.2f},".format(dayup))
