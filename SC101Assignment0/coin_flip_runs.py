"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:
	"""
	print("Let's flip a coin!")
	run = int(input("Number of runs: "))
	count = 0
	last = 2
	streak = 0
	# h = 0, t = 1
	while True:
		if run == count:
			break
		ans = r.randrange(2)
		if ans == 0:
			print("H", end="")
		else:
			print("T", end="")
		if last == ans:
			if streak == 0:
				count += 1
			streak += 1
		else:
			streak = 0
			last = ans

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
