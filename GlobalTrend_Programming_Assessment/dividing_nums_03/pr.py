
# Write a Python function that divides two numbers and handles the case where the divisor is zero by returning a custom error message.


def dividing_nums(numerator, denominator):

    if denominator == 0: # to check if the denominator is zero or not
        return "Error: cannot divide by Zero"

    else: 
        result = numerator/denominator
        return result

print(dividing_nums(25, 5))     
print(dividing_nums(25, 0))     

