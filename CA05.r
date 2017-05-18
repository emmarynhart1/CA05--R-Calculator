add <- function (x,y) {
  return (x+y)
}


subtract <- function(x,y) {
  return(x-y)
}

multiply <- function(x,y) {
  return(x*y)
}

divide <- function(x,y) {
   if (y==0){
  	return("error")
    } else }
  	return(x/y)
    }
}

exponent <- function(x,y) {
  return(x**y)
}

squareroot <-function(x) {
  return(sqrt(x))
}

cosine <- function(x) {
  return (cos(x*pi/180))
}

sine <- function(x) {
  return (sin(x*pi/180))
}

tangent <- function(x) {
  if (x %% 180 ==0){
     return (0)
   } else if (x%% 90 ==0){
     return ("error")
   } else {
     return (tan(x*pi/180))
   }
}

factorial <- function(x) {
   if (x<= 1) {
		return (1)
   }  else {
	return(x * factorial(x-1))
   }
	
}

loop <- TRUE
	while(loop){

print ("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponent")
print("6.Squareroot")
print("7.Cos")
print("8.Sin")
print("9.Tan")
print("10.Factorial")

choice = as.integer(readline(prompt = "Enter choice[1/2/3/4/5/6/7/8/9/10]: "))

num1 = as.integer(readline(prompt = "Enter first number: "))
num2 = #as.integer(readline(prompt = "Enter second number: "))
	if(choice <= 5){
	num2= as.numeric(readline(prompt="Enter second numer:"))
	}

operator <- switch(choice,"+","-","*","/","**","Sqrt","Cos","Sin","Tan","Factorial")
result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2), exponent(num1,num2), squareroot(num1),cos(num1),sin (num1), tan(num1), factorial(num1))

print (paste(num1, operator, num2, "=", result))

ask = readline(prompt = "Would you like to do another calculation? Yes or No")
	if (ask != "Yes") 
	loop <- FALSE
	print ("Thank You, Goodbye!")
	} 