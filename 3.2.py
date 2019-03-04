# daydayupq2
dayfactor = 0.01
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("dayup:{:0.2f},daydown:{:0.2f}".format(dayup, daydown))
