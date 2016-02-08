def main():
	a = [1,3,54,32,12,34,5,9]
	
	y = list(map(lambda x: x+2 , a))
	print (y)
	
	z = list(filter(lambda x: x%2 , a))
	print (z)
	
	# w = functools.reduce( p if (p > b ) else b , [1,3,54,32,12,34,5,9])
# 	print (w)
# i couldnt get how i could use reduce in python 3 ,
# apparently they removed it and theres very little documentation.

if __name__ == "__main__":main()