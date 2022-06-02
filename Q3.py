def check_math(list_of_equations):
    """The function returns True if all math equations are mathematically correct, and False if at least one of the equations is mathematicall wrong. If the list is empty, the function returns True"""

    for equation_string in list_of_equations:
        list_of_char = equation_string.split()     # split into a list of individual character
        final_string = " ".join(list_of_char)       # join elements of string using empty string
        for char in final_string:
            print(char)
        print(final_string)
        #operator = final_list[1]         # remove leading and trailing whitespaces for each char
        #n1 = int(final_list[0])
        #n2 = int(final_list[2])
        #test_answer = int(final_list[-1])

    # Create a dict with lambda expression to use the operator through key-value pair
        dict_of_operator = {'+': lambda n1,n2:n1+n2, '-':lambda n1,n2:n1-n2, '*':lambda n1,n2:n1*n2, '//':lambda n1,n2:n1//n2, '%': lambda n1,n2:n1%n2 }
        #actual_answer = dict_of_operator[operator](n1,n2)
        #if actual_answer == test_answer:
        #    return True
        #else:
        #    return False


print(check_math([" 3 +5 =9", "4 * 3 = 12 "]))

# LEFTOVER ISSUE: Need find a way to separate e.g: = from =9 or + from +5