1. What is the alternative implementation of function overloading in python?

Default Arguments: You can use default values for function parameters to handle different cases within a single function.
Variable Number of Arguments: Use *args and **kwargs to handle a variable number of positional and keyword arguments.
Single Dispatch Generic Functions: Use the functools.singledispatch decorator to create functions that can be dispatched based on the type of the first argument.


2. Why there is no implicit type casting in python?

Python follows the principle from the Zen of Python: "Explicit is better than implicit." Implicit type casting can lead to code that behaves in unexpected ways, making it harder to understand and debug. By requiring explicit type conversions, Python encourages clearer and more predictable code.


3. Why there is no ++ and -- (increment/decrement) operators in python?

 * Simplicity and Readability
Python emphasizes readability and simplicity. The ++ and -- operators are often seen as less clear because they can be used in both prefix and postfix forms, potentially leading to confusion or errors in complex expressions. Instead, Python promotes clarity by using explicit operations.

  * Unification of Syntax
Python's design philosophy favors consistency and avoiding special-case syntax where possible. The increment and decrement operations can be performed using explicit syntax, which fits well with Python’s focus on clear code
   
   * Using += and -= makes the intent clear and is consistent with other operations in Python.


4. What is the difference between @static method and @class method?

    * First Argument:

        @staticmethod: No implicit first argument.
        @classmethod: The first argument is cls, which represents the class.

    * Access to Class/Instance Data:

         @staticmethod: Cannot access or modify class or instance data.
         @classmethod: Can access and modify class data but not instance-specific data.
    * Use Cases:

         @staticmethod: For utility functions that are logically related to the class but do not need to interact with class or instance data.
         @classmethod: For methods that need to interact with or modify class-level data, or for factory methods that create instances of the class.

5. What is the difference between __new__() and __init__() ?

       *  __new__() is responsible for creating a new instance of a class. It is the method that actually allocates memory for the object and returns the new instance.
       *  __init__() initializes a new instance that has already been created by __new__(). It sets up the initial state of the object and can modify instance attributes.
6. What is the syntax to use switch case in python? Give an example?
      def switch_case(value):
    if value == 1:
        return "One"
    elif value == 2:
        return "Two"
    elif value == 3:
        return "Three"
    else:
        return "Default case"
