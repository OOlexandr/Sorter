from multiprocessing import Process, Manager

def factorize_inner(num, result, i):
    for f in range(1, (num//2+1)):
        if not num % f:
            result[i].append(f)
    result[i].append(num)
    

def factorize(*args):
    with Manager() as manager:
        factors = manager.list()
        for i in args:
            factors.append(manager.list())
        processes = []
        i = 0
        for n in args:
            fact = Process(target=factorize_inner, args=(n, factors, i))
            fact.start()
            processes.append(fact)
            i += 1
        for p in processes:
            p.join()

        result = []
        for f in factors:
            result.append(list(f))
    return result
