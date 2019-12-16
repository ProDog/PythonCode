from multiprocessing import Pool

def calSquare(x):
    return x*x

if __name__=='__main__':
    with Pool(5) as p:
        print(p.map(calSquare,[2,4,6,7,8,10,-5,0,26]))