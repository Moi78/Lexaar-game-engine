import time

def test() :
        start = int(time.time()*1000)
        time.sleep(2)
        stop = int(time.time()*1000)
        print(stop-start)

test()