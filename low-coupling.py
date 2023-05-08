# Welcome to this attempt at low coupling
# - Amber Crimsonwood 🏳️‍⚧️

def function_that_does_a_thing(variable1, variableB):
    if isinstance(variable1, int) and isinstance(variableB, int):
        return variable1 + variableB
    else:
        raise TypeError("no!!! it must be int! >:c")
        return 0;

def display_in_fancy_way(thingToDisplay):
    if thingToDisplay is not None:
        return f"""
        ===============================
                {thingToDisplay}
        ===============================
        """
    else:
        raise ValueError("you are stinky!! no parameter found ):<")

print(display_in_fancy_way(function_that_does_a_thing(4, 69)))