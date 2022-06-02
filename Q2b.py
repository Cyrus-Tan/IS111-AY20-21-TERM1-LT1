def get_max_of_min(list_of_num_tuples):
    """function returns the maximum of the minimum values in these tuples."""
    list_of_min_values = []              # Create empty list

    for tuple_of_numbers in list_of_num_tuples:                       # iterate through each tuple in the list
        list_of_numbers = list(tuple_of_numbers)                      # convert the tuple to list
        tuple_minimum_value = list_of_numbers[0]                      # assign first element of the list to current minimum value
        for number in list_of_numbers:                                                    # iterate through list of numbers
            if number < tuple_minimum_value or number == tuple_minimum_value:             # compare number in the list with current tuple_minimum_value
                tuple_minimum_value = number                                              # number will be current tuple_minimum_value if its smaller than previous
        list_of_min_values.append(tuple_minimum_value)                                    # add each minimum value to the list

    if len(list_of_min_values) == 0:                # if empty list, return None
        return
    elif len(list_of_min_values) > 0:               # only returns a value if list is not empty
        max_value = list_of_min_values[0]           # let first number be max value among the final 3 numbers


### METHOD 1: Compare items (integers) among a list to find max value  ( Not as good method because have to specify index)

#       for number in list_of_min_values:             # iterate through the list of min values
#           if list_of_min_values[1] > max_value:
#               max_value = list_of_min_values[1]     # will replace max value if second number > first number
#           elif list_of_min_values[2] > max_value:
#               max_value = list_of_min_values[2]     # will replace max value if third number > second number

### METHOD 2: Same as METHOD 1, but we replace list_of_min_values[1] with number ----> we don't need to use list indexing

        for number in list_of_min_values:                # Diff between METHOD 2 AND 3: 2 loops through the elements of the list
            if number > max_value:                       #                              while 3 loops through the index of the list
                max_value = number


### METHOD 3: Compare items (integers) among a list to find max value ( BETTER Method because we don't need to specify index, will loop through length of the list)

#       for index in range(len(list_of_min_values)):      # loop through the length of the list
#           if list_of_min_values[index] > max_value:     # index here refers to current index we are looping through
#               max_value = list_of_min_values[index]     # will

        return max_value


#print(get_max_of_min([(1, 5, 3), (5, 1, 9), (4, 10, 19)]))
#print(get_max_of_min([(-15, 20, -40), (-4, -1, -4)]))
#print(get_max_of_min([(3, -9, 0)]))                       # produces -9 because its the only number appended to list_of_min_values, since only one tuple
#print(get_max_of_min([]))