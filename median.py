# Week 1 Median Exercise.
# Author: Romina Todor.
# Date: 16/10/2023.
# Student Number: k22004116

# Step 1: Find how many items in list.
# Step 2: Sort list in ascending order.
# Step 3: Find no. times list size is divisible by 2 and subtract one to use as index pointer (number in list): lowerbound.
# Step 4: Add 1 to find index pointer (number in list) after lowerbound: upperbound.
# Step 5: If even no. items in list find median as no. inbetween.
# Step 6: If odd no. items in list find median as middle no.
# Step 7: Check: break if not valid.
# Step 8: Output median.

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        input_string=input().strip()
        numbers = [float(value) for value in input_string.split(",")]
        # Step 1: 
        size = len(numbers)
        # Step 2: 
        numbers.sort()
        # Step 3:
        lowerBoundIndex = int((size//float(2)) - float(1))
        lowerBound = numbers[lowerBoundIndex]
        # Step 4:
        upperBoundIndex = int(lowerBoundIndex + float(1))
        upperBound = numbers[upperBoundIndex]
        # Step 5:
        if size%2 == 0:
            median = (lowerBound + upperBound)/float(2)
        # Step 6:
        else:
            median = upperBound
        # Step 7:
        print(f'{int(median)} is the median.\n')
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
