def get_sum_of_digits(my_str):
    """The function sums up all the digits found in the string and returns the sum as an int"""
    list_of_characters = list(my_str)
    sum_value = 0
    for character in list_of_characters:
        if_is_digit = character.isdigit()        # check if character is a digit
        if if_is_digit:                          # if is a digit ( if True:)
            sum_value += int(character)
    return sum_value


#print(get_sum_of_digits('1234'))
#print(get_sum_of_digits('SMU1-2-3-4'))
#print(get_sum_of_digits('32-4*5(0)36'))
#print(get_sum_of_digits('SMU-SIS'))
#print(get_sum_of_digits(''))