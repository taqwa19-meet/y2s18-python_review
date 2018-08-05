# We your solution for 1.4 here!

def is_prime(x):
	t=1
	while t<x:
		if x%t==0:
			if t!=1 and t!=x:
				return False
		t=t+1
	return True	

print(is_prime(5191))	

