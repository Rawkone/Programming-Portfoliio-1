def f():
    x = 22
 
# Call the function
f()
# This fails, x only exists in f()
print(x)

# Create the x variable and set to 44
x = 44
 
# Define a simple function that prints x
def f():
    x += 1
    print(x)
 
# Call the function
f()

Proper use of a main function
def main():
    print("Hello world.")
 
if __name__ == "__main__":
    main()