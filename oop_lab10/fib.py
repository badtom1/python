import time 

def timeit(func):
	def timed(*args,**kw):
		print("before the timeit decorator")
		ts=time.time()
		result=func(*args,**kw)
		te=time.time()
		minutes,seconds=divmod((te-ts),60)
		print(minutes,seconds)
		print("time taken %8.2f" %((te-ts)*10**60))
		print("after the timeit decorator")
		return result
	return timed

@timeit
def fib():
	a,b=0,1
	while(1):
		yield a
		a,b=b,a+b
n=int(input("enter the size of fibonacci series"))

f=fib()

for i in range(n):
		print(next(f))
