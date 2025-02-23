from typing import Union

# ***************************************************************************************
# Handling exceptions
# ***************************************************************************************

def divison(divisor: float) -> Union[str, float]:
    try:
        return 100 / divisor
    except ZeroDivisionError as e:
        return "Dividing by zero is not allowed"

# NOTE: Using a bare "except:" syntax is a bad practice
# The application won't crash simply when it was required to

print(divison(0))

# ***************************************************************************************
# Handling multiple exceptions
# ***************************************************************************************

from typing import Union

def funnier_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"

# for val in (0, "hello", 50.0, 13):
#     # NOTE: "end" turns the default trailing newline into a space so 
#     # that it’s joined with the output from the next line.
#     print(f"Testing {val!r}:", end=" ")
#     print(funnier_division(val))

# ***************************************************************************************
# Stacking the except clause
# ***************************************************************************************

def funniest_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError as e:
        print("No, No, not 13!", end = "")
        # It will raise the exception again we will
        # still get the original stack trace on the console.
        raise
    except Exception as e:
        print(f"Caught some other error: {e.__class__.__name__}")

funniest_division(13)
