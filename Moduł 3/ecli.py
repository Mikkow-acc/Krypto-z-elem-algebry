from pmc import *
from random import randrange, getrandbits, randint

def gen(k):
	p = generate_prime_number(k)
	return p

def generate(p):
	flag = False
	while (flag != True):
		A = randint(2, p)
		B = randint(2, p)
		delta = (4 * binpow(A, 3, p)) % p + (27 * binpow(B, 2, p)) % p
		if delta != 0:
			flag = True
	return A, B

def change_parameters(A, B, p):
	A = A
	B = B
	p = p

def random_point(A,B,p):
	flag = False
	while (flag != True):
		x = randint(2, p)
		xd = x**3 + A * x + B
		if eulerTest(xd, p):
			y = binpow(xd, (p+1)//4, p)
			flag = True
	return x, y
