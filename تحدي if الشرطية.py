Number1 = int(input("Please Enter Number 1 "))
Number2 = int(input("Please Enter Number 2 "))
OpeartionType = input("Please Enter The Opeartion Type ")

if OpeartionType == "+" :
   print(Number1 + Number2)
elif OpeartionType == "-" :
  print(Number1 - Number2)
elif OpeartionType == "*" :
  print(Number1 * Number2)
else :
  print("We don't support this operation")
  
print("Thanks for using our software")