import turtle as tt
'''
tt.fd(50)
tt.seth(90)
tt.fd(50)
tt.seth(180)
tt.fd(50)
tt.seth(270)
tt.fd(50)
'''
for i in range(4):
    tt.seth(90*i)
    tt.fd(100)

tt.done()
