import math

def isPrime(n):
	if not n % 2: return n == 2
	if not n % 3: return n == 3
	if not n % 5: return n == 5
	for p in range(7, int(math.sqrt(n))+1, 2):
		if not n % p: return False
	return True

def six_prime(n):
	six_min = six_max = False
	if isPrime(n) and isPrime(n+6):
		six_max = True
	if isPrime(n) and isPrime(n-6):
		six_min = True
	if six_min:
		return n-6
	elif six_max:
		return n+6
	elif six_min or six_max:
		return n-6
	else:
		return False

def main():
	num = int(input())
	res = six_prime(num)
	if res:
		print('Yes')
		print(res)
	elif res == False:
		print('No')
		attempt = num
		while not six_prime(attempt):
			attempt += 1
		print(attempt)


if __name__ == '__main__':
	main()
