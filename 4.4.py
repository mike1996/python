try:
    weight, height = eval(
        input("please input your weight(kg) and height(m) with ',':"))
except NameError:
    print("wrong input")
bmi = weight/pow(height, 2)
print("BMI is:{:.2f}".format(bmi))
if bmi < 18.5:
    who = cho = "偏瘦"
elif 18.5 <= bmi < 24:
    who, cho = "正常", "正常"
elif 24 <= bmi < 25:
    who, cho = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, cho = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, cho = "偏胖", "肥胖"
else:
    who, cho = "肥胖", "肥胖"
print("BMI分类为：WHO{0} 国内{1}".format(who, cho))
