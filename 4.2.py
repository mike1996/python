score = eval(input("请输入一个成绩:"))
if score >= 60 and score < 70:
    grade = 'D'
elif 70 <= score < 80:
    grade = 'C'
elif 80 <= score < 90:
    grade = 'B'
elif score <= 90 <= 100:
    grade = 'A'
else:
    grade = '不合格'
print("输入成绩属于{}".format(grade))
