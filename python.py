# Square(n) sum
# Create a function that given a list of integers squares each EVEN number 
# passed into it and then sums the results together.

# Example Input: [1, 2, 2]
# Example Output: 8
# Explanation: 2 is the only even # in the array so 2^2 = 4 + 2^2 = 4 = 8


# Example Input: [3, 4, 5, 8]
# Example Output: 80
# Explanation: 4 & 8 are even so 4^2 = 16 + 8^2 = 64 = 80

def squareEven(arr):
    new_num = 0
    for n in arr:
        if n % 2 == 0:
            new_num += n ** 2
    return new_num

print(squareEven([2,2]))


    