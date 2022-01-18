'''
Exception hierarchy
The class hierarchy for built-in exceptions is:
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning

Error or Bugs:
As a human we commit several errors. A software developer is also a human being
and hence prone to commit error either in the design of the software or in the
code.The errors in the software called 'bugs' and the process of removing them
is called 'debugging'.

Errors in Python:
--> compile time errors
--> Runtime errors
--> Logical errors

Compile time errors:
--> It is basically syntax based error like sometimes we forget to put colon on
end of the conditional statements.
--> Eventually it will identify by the python compiler and line number along
with the error description is displayed by the python compiler.
    -> Syntax error - invalid syntax
    -> Indentation error - unexpected indent   are the compile time errors.

Runtime Errors:
--> Runtime errors are happen when PVM is unable execute the byte code.
--> for instance, insufficient memory to store something or inability of PVM to
execute some statements comes under runtime errors.
--> It is detected by PVM at runtime not by Compiler.
        -> index error
        -> Type error  are some of the runtime errors.

Logical Errors:
--> These errors depict flaws in the logic of the program.
--> It is based on the programmers logic they have to take care of it.



























'''
# Compile time errors:
# Ex:1
x = 1
# if x = 1
print('colon is missing')
# SyntaxError: invalid syntax
# IndentationError: unexpected indent


# RuntimeError:
# Ex 1:
def name(a, b):
    full_name = a + b
    return full_name


# obj = name('Karthi', 38)
obj = name('Karthi', 'Ramesh')
print(obj)  # TypeError: can only concatenate str (not "int") to str

# Ex 2:

employee = ['Karthi', 'kumar', 'Shiva', 'Karthik']
# print(employee[4]) # employee[4] IndexError: list index out of range
print(employee[2])


# Logical Error:
























