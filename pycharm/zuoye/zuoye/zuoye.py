def f():
    a = []
    for i in range(5):
        a.append(lambda x: i*x)
    return a
#
#
# t = f()
# print(t[0](2), t[1](2), t[2](2))
# x = 3
# print(x==3)
# print(x)
# print(x==3)
# print(x=3)
# pf = lambda a, b=2: a + b
# print(pf(b=8, a=5
# a = [1, 2, ['a', 'b']]
# b = a
# # a.insert(0, 3)
# # a[-1].append(3)
# # print(b)
# a = {1,2,3,3,4,5},
# a = a – {1,2,3}
def he(n):
    sun = 0
    for x in range(1,n+1):
         if x%2 == 0:
              sun+=x
    return sun
print(he(10))