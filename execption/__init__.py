# Exception Hierarchy:
#
# BaseException
#     |
#     └── Exception
#         |
#         └── StandardError
#             |
#             ├── ArithmeticError
#             │
#             ├── EnvironmentError
#             │   ├── IOError
#             │   └── OSError
#             │
#             ├── SyntaxError
#             │
#             └── RuntimeError
#
# This represents the inheritance hierarchy of Python's built-in exceptions:
# - BaseException is the root of the exception hierarchy
# - Exception inherits from BaseException and is the base class for all built-in exceptions
# - StandardError inherits from Exception and is the base class for all built-in error exceptions
# - ArithmeticError, EnvironmentError, SyntaxError, and RuntimeError are concrete error types
# - EnvironmentError further specializes into IOError and OSError for system-related errors

# Almost all the exceptions extend from the Exception class
# - SystemExit
# - KeyboardInterrupt
# Both of them extends from "BaseException"
# These are extended from "BaseException" because they are not meant to be caught by the user code.
# And we don't want them to be caught in a generic "except Exception:" block.

# NOTE:
# When we use the "except:" clause without specifying any type of exception, 
# it will catch all subclasses of BaseException; which is to say, it will catch all exceptions, 
