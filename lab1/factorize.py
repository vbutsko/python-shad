def factorize(x):
	result = [];
	div = 2;
	while ( div ** 2 <= x):
		if not x % div :
			result.append(div);
			x //= div;
		else:
			div += 1;
	if x > 1:
		result.append(x);
	return result;

num = int(input());
dividers = factorize(num);
print (" ".join(map(str, dividers)));