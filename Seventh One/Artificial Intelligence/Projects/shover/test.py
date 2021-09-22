class test:
    def __init__(self, a):
        self.a = a
    def ret(self):
        return self.a

new = test([1,2,3])

print(new.a)
t = new.ret()
t = [1,2]
new.a = t
print(new.a)
