def Arguments(argument):
    if argument % 3 ==0 and argument % 5 == 0:
        return "FezzBuzz"
   
    elif argument % 5 == 0:
        return "Buzz"
    elif  argument % 3 == 0:
        return "Fizz"
    else: 
        return "not Fizz or Buzz"
    
argument = input ("plz enter your number")
if(argument.isdigit()):
    argument = int(argument)  
    print(Arguments(argument));


    
        