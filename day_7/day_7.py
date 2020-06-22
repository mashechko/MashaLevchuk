from pip._vendor.msgpack.fallback import xrange

for x in xrange(5, 10):
    if x % 2 == 0:
        x = x * 2
        print(x)
    else:
        x += 1
        print(x)