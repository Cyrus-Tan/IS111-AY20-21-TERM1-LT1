def trace_contacts(patient, history):
    no_more_people = False                 # create flag variable
    close_contact_infected = []
    infected_day = -7                    # for first person
    #while not no_more_people:              # while True

    for each_tuple in history:
        while not no_more_people:  # while True
            if patient in each_tuple:

                if patient == each_tuple[0]:
                    day_met = each_tuple[-1]
                    value_diff = infected_day - day_met
                    if value_diff == -1:
                        pass                         # person not infected
                    elif -7 < value_diff < -1:           # value_diff from -6 to -2
                        close_contact_infected.append(each_tuple[1])
                        infected_day = day_met                          # new infected day of second person will be day met between first and second
                        if each_tuple[1] in each_tuple and patient not in each_tuple:      # compare third person
                            if value_diff == -1:
                                no_more_people = True                       # stop loop
                            elif -7 < value_diff < -1:
                                no_more_people = False
                elif patient == each_tuple[1]:
                    day_met = each_tuple[-1]
                    value_diff = infected_day - day_met
                    if value_diff == -1:
                        pass
                    elif -7 < value_diff < -1:
                        close_contact_infected.append(each_tuple[0])
                        infected_day = day_met
                        if each_tuple[1] in each_tuple and patient not in each_tuple:      # compare third person
                            if value_diff == -1:
                                no_more_people = True                       # stop loop
                            elif -7 < value_diff < -1:
                                no_more_people = False
            else:
                no_more_people = True
    return close_contact_infected

print(trace_contacts(patient="Jason", history=[("Jason", "Gideon", -3), ("Zac", "Yacob", -3), ("Gideon", "Brian", -1), ("Cindy", "Gideon", -2), ("Darren", "Jason", -5), ("Jason", "Vivian", -6)]))


# TRIED changing from Q4a.py but still doesn't work

