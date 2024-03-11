from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


print('-------')


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()

# f()
# g()
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
# f()
# Error: <function g at 0x7fabdc243ee0> call too many times
