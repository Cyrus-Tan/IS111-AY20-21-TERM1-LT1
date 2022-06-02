def trace_contacts(patient, history):
    close_contact_infected = []
    #dates_list = []
    for each_tuple in history:                                                  # iterate through each tuple
           # check close contact of patient during patient's infectious period (-5 to -1)
        if patient in each_tuple:                                               # check those that contact with patient
            if patient == each_tuple[0]:                                        # if patient is first name in tuple
                infectious_period_day = each_tuple[-1]                          # get the last element(the day)
                if infectious_period_day > -6 and infectious_period_day < 0:    # if number is from -5 to -1
                    close_contact_infected.append(each_tuple[1])                # second name in tuple is infected
                   #dates_list.append(infectious_period_day)
            elif patient == each_tuple[1]:                                            # if patient is second name in tuple
                infectious_period_day = each_tuple[-1]
                if infectious_period_day > -6 and infectious_period_day < 0:
                    close_contact_infected.append(each_tuple[0])                      # first name in tuple is infected
                    #dates_list.append(infectious_period_day)


#        for close_contact in close_contact_infected:
#        #for date in dates_list:
#            #for each_tuple in history:
#            if close_contact in each_tuple and patient not in each_tuple:     # if close contact met a third person (someone other than patient)
#                if close_contact == each_tuple[0]:                            # if close contact is first name in tuple
#                    secondary_infectious_period_day = each_tuple[-1]
#                    if abs(infectious_period_day - secondary_infectious_period_day) > 1:
#                        close_contact_infected.append(each_tuple[1])          # third person infected is second name in tuple
#                elif close_contact == each_tuple[1]:                          # if close contact is second name in tuple
#                    secondary_infectious_period_day = each_tuple[-1]
##                        close_contact_infected.append(each_tuple[0])          # third pereson infected is first person name in tuple

    return close_contact_infected


#print(trace_contacts(patient="A", history=[("B", "A", -5), ("C", "A", -1), ("B", "C", -2)]))
print(trace_contacts(patient="Jason", history=[("Jason", "Gideon", -3), ("Zac", "Yacob", -3), ("Gideon", "Brian", -1), ("Cindy", "Gideon", -2), ("Darren", "Jason", -5), ("Jason", "Vivian", -6)]))

# LEFTOVER ISSUE: Only able to get Gideon and Darren, can't get Brian
#                 Need to find a way to get the third person (change the number/days from first to next person)