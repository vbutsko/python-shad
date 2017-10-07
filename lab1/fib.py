def fib(n):
	fib_n_2 = 0;
	fib_n_1 = 1;
	temp = 0;
	for __ in range(n):
		temp = fib_n_1 + fib_n_2;
		fib_n_2 = fib_n_1;
		fib_n_1 = temp;
	return fib_n_2;

n = int(input());
print( fib(n) );
