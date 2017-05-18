#Function for Min
def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)
	
print max([47, 11,42,13])

#Function for Max
def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)
	
print min([47, 11,42,13])

#Function for even numbers
def is_even(values):
	return filter(lambda x:x % 2 == 0, values)
	
print is_even([47,11,42,13])

#Function for odd numbers
def is_odd(values):
	return filter(lambda x:x % 2, values)
	
print is_odd([47,11,42,13])

#Function to Add
def add(values):
	return reduce(lambda a,b: a+b, values)
	
print add([47,11,42,13])

#Funtion to convert to Fahrnheit
def fahrenheit(t):
    return ((float(9)/5)*t + 32)
temp = (36.5, 37, 37.5, 39)
F = map(fahrenheit, temp)
print F
	

#Function to convert to Celsius	
def celsius(t):
    return (float(5)/9*(t - 32))
temp = (36.5, 37, 37.5, 39)
C = map(celsius, F)
print C

#Function to Divide
def divide(values):
	return reduce(lambda a,b: a/float(b) if (b !=0 and a != 'Nan')
		else 'Nan', values)
	
print divide([47,11,42,13])

#Function to Multiply
def multiply(values):
	return reduce(lambda a,b: a*b, values)
	
print multiply([47,11,42,13])

#Cross Product
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print coloured_things

#Generator 
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter >= n): return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(5)
for x in f:
    print x,
print

#Pythagorean triples
n=300
pyt_triples = []
for x in range (1,n):
	for y in range(x,n):
		for z in range(y,n):
			if x**2 + y**2 == z**2:
				pyt_triples.append((x,y,z))
print pyt_triples