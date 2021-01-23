# Return the drink preference of the specified patron, regardless of parameter character format.


def get_drink_by_profession(param):
    input = {"Jabroni": "Patron Tequila", 
            "School Counselor": "Anything with Alcohol",
            "Programmer": "Hipster Craft Beer",
            "Bike Gang Member": "Moonshine",
            "Politician": "Your tax dollars",
            "Rapper": "Cristal"}
    

    lower_param = param.lower()
    lower_input = {k.lower(): v for k, v in input.items()}
    if lower_param in lower_input:
        return lower_input.get(lower_param)
    else:
        return "Beer"


print(get_drink_by_profession("Rapper"))