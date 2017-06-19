#1
def sum1(a, b, c):
 return(a + b + c)
print(sum1(10, 11, 12))

#2
def increase (x):
 return (x + 1)
x = 10
print("X is", x, " I will now increase x.")
increase (x)
print("X is now", x+1)

#3
def print_hello():
 print("Hello")
 
print_hello()

#4
def count_to_ten():
 for i in range(11):
  print(i)
count_to_ten()

#5
def sum_list(list):
 return sum(list)
list = [45, 2, 10, -5, 100]
print(sum_list(list))

#6
def reverse(text):
 result = ""
 text_length = len(text)
 for i in range(text_length):
  result = result + text[i * -1 - 1]
 return result
text = "Programming is the coolest thing ever."
print(reverse(text))

#7
def get_user_choice():
 while True:
  command = input("Command: ")
  if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
    return command
   
  else:
   print("Hey, that's not a command. Here are your options:" )
   print("f - Full speed ahead")
   print("m - Moderate speed")
   print("s - Status")
   print("d - Drink")
   print("q - Quit")
user_command = get_user_choice()
print("You entered:", user_command)



