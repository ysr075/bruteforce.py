import random
import time
import os

def main():
	i = 0
	while True:
		i = i + 1
		list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '&', '(', ')', '–' , '[', '{', '}', ']', ':' ,';', ',' ,'?', '/', '*', '`', '~', '$', '^', '+', '=', '<', '>', '“']
		random_a = random.choice(list)
		random_b = random.choice(list)
		random_c = random.choice(list)
		random_d = random.choice(list)
		random_e = random.choice(list)
		random_f = random.choice(list)
		random_g = random.choice(list)
		random_h = random.choice(list)
		random_i = random.choice(list)
		random_j = random.choice(list)
		print("case " + str(i) + " = " + random_a + random_b + random_c + random_d + random_e + random_f + random_g + random_h + random_i + random_j)
		time.sleep(0.01)

if __name__ == '__main__':
	main()
