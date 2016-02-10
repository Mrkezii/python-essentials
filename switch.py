def main():
	choice = dict(
		one = 'first',
		two = 'second',
		three = 'third',
		four = 'four'
	)

	v = 'one'
	print(choice.get(v, 'put in a valid number'))

if __name__ == "__main__":main()