from itertools import combinations

def get_factor(number):
	return list(filter(lambda x: not number%x, range(1, number+1)))

def sum_factor_combine(factors):
	return list(map(sum, combinations(factors, 4)))

def isBeautiful(number, combine):
	flag = False
	for com in combine:
		if (number % com == 0) or (com % number == 0):
			flag = True
			break
	return flag


def main():
	count = int(input())
	number = list(map(int, input().split()))
	
	for num in number:
		if isBeautiful(num, sum_factor_combine(get_factor(num))):
			print('Yes')
		else:
			print('No')

if __name__ == '__main__':
	main()