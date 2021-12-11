x = int(input("Число: "))
def sqrt(x):
    
    def sqrtIter(guess):
        if goodEnaugh(guess):
            return guess
        else:
            return sqrtIter(improve(guess))
        
    def improve(guess):
        return average(guess, x/guess)
    
    def average(x, y):
        return (x+y)/2
    
    def goodEnaugh(guess):
        if(abs(guess**2-x)<0.001):
            return 1
        else:
            return 0
        
    return sqrtIter(1.0)
print(sqrt(x))
