# Using 'return' in a function to get squares of numbers up to n
def get_squares_with_return(n):
    squares = []
    for i in range(1, n+1):
        squares.append(i * i)
    return squares

# Using 'yield' in a generator to get squares of numbers up to n
def get_squares_with_yield(n):
    for i in range(1, n+1):
        yield i * i

# Using the function with 'return'
squares_return = get_squares_with_return(5)
print(f"Using return: {squares_return}")

# Using the generator with 'yield'
# squares_yield = list(get_squares_with_yield(5))
# print(f"Using yield: {squares_yield}")