p = float(input('Enter current bank balance:'))
i = float(input('Enter interest rate:'))
t = int(input('Enter the amount of time that passes:'))
x = 1

def interest():
	f = p * (x + i)**t
	#print(a)
	print(f'{f}')
interest()