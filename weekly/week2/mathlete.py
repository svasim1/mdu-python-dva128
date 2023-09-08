# Print header
print(".: MATHLETE v2.0 :." + "\n" + "-------------------")

# Define variables
numbers_entered = []
sum_total = 0

while True:
    input_number = input('> ')
    
    if input_number.lower() == 'exit':
        break
    
    try:
        input_number = int(input_number)
        numbers_entered.append(input_number)
        sum_total += input_number
    except ValueError:
        print('ERROR: Invalid number')

cardinality = len(numbers_entered)
mean_value = sum_total / cardinality if cardinality > 0 else 0

# Print output
print("-------------------" + "\n" + f"Cardinality: {cardinality} " + " \n" + f"Sum: {sum_total} " + "\n" + f"Mean value: {mean_value} ")

