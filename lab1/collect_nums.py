def collect_num(a,b):
	number_str = "";
	for i in range(b+1):
		number_str += str(a+i);
	number_int = int(number_str);
	return number_int ** 10;


a, b = map(int, input().split(' '));

print (collect_num(a, b));