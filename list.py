def main():
	x = (1,2,3)
	print(type(x), x)
	y = [1,2,3]
	y.append(9)
	y.append(4)
	y.insert(2,8)
	print(type(y), y)

if __name__ == "__main__" : main()