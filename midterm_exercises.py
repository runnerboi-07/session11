print(type(3|2)) # Int
print(type(print("xx"))) # NoneType
print(type(~3)) # Int
print(type(2*3)) # Int
print(type(2.0*3.0)) # Float
print(type(2+3)) # Int
print(type(6/2)) # Float
print(type(2 != 3)) # Boolean
print(type(5 or 6)) # Int
print(type(print)) # Fn
print(type(print(2*2))) ##### NoneType #####
print(type("abc".find)) # Fn
print(type("bubu"*2)) # String

try:
    print(type("bubu"*(4/2))) # Error
except:
    print("error")

print(type(["abc", 2])) # List
print(type("abc"[2])) # String
print(type("abcabcabc".split("a"))) # List

# Q4 - Write a function that takes the name of a text file as parameter.
# Print out the 3- letter words that start with “b”

# Q5 - Write a function that takes an integer as parameter and returns a list of all the divisors of that number
def divisor_finder(integer):
    """
    Function that finds all divisors of given integer
    :param integer: Integer value inputted by user
    :return: List of divisors
    """
    div_list = []
    for i in range(1, integer + 1):
        if integer % i == 0:
            div_list.append(i)
    return div_list

print(divisor_finder(102))

# Q6 - Write a function that forces the user to enter a multiple of 6 number.
# Use try, except to catch invalid inputs. Return that number

