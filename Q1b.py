def is_compatible(patient_group, donor_group):
    """function returns True if the donor’s blood group is compatible and False otherwise."""
    if patient_group == "A":
        if donor_group == "A" or donor_group == "AB":
            return True
        else:
            return False
    elif patient_group == "B":
        if donor_group == "B" or donor_group == "AB":
            return True
        else:
            return False
    elif patient_group == "AB":
        if donor_group == "AB":
            return True
        else:
            return False
    elif patient_group == "O":
        if donor_group == "O" or donor_group == "AB" or donor_group == "A" or donor_group == "B":
            return True
        else:
            return False

#print(is_compatible("B", "AB"))
#print(is_compatible("O", "A"))
#print(is_compatible("AB", "O"))