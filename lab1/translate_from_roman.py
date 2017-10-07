alphabet = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D', 900:'CM', 1000:'M'}

def translate_from_roman(number_str):
	result = 0
	adds = sorted(alphabet, reverse=True)
	for add in adds:
		while number_str.startswith(alphabet.get(add)):
			result += add
			number_str = number_str[len(alphabet.get(add)):len(number_str)]
	return result

print(translate_from_roman(input()))