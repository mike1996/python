# 循环
# %% continue
for c in "PYTHON":
    if c == "T":
        continue
    print(c, end="")
# %% break
for c in "PYTHON":
    if c == "T":
        break
    print(c, end="")
# %%
s = "PYTHON"
while s != "":
    for c in s:
        print(c, end="")
    s = s[:-1]
# %% break仅仅能退出最内层
s = "PYTHON"
while s != "":
    for c in s:
        if c == "T":
            break
        print(c, end="")
    s = s[:-1]
# %%
s = "PYTHON"
while s != "":
    for c in s:
        if c == "T":
            continue
        print(c, end="")
    s = s[:-1]
# %% 循环与else
# 当循环没有被break推出时,执行else
for c in "PYTHON":
    if c == "T":
        continue
    print(c, end="")
else:
    print("\n正常退出")
