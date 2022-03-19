from multiprocessing import Process
class testAsynch():
    
    def function_1(x):
        return float(x)
    
    def function_2(y):
        return float(y)
    


def f():
    f1 = testAsynch.function_1(2)
    f2 = testAsynch.function_2(4)

if __name__ == '__main__':
    p = Process(target=f, args=())
    p.start()
    p.join()