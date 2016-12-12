# About
A quick and simple debug decorater which lets you toggle stdout debug within a function without needing an extra argument for the function and unnecessary if else statements. Especially useful for debugging quick scripts and prototypes. When debug is disabled, no resources are spent on logging unnecessarily.

Supported on Python2 and Python3.

**WARNING-1**: Do not use this module if you are already using the `logging` module for other critical logging purposes since it may intefere with it. This is currently a solution only meant for simple yet frustrating use cases. If you are using the `logging` module, please change the code as you please to integrate it into your work.

**WARNING-2**: You will no longer be able to pass an argument named `debug` to your functions since this module will recognize that argument for itself and remove it from the arguments.

# How To Use - (Carefully notice the debug argument)

### How you would have used debug before
```python
def sum(a, b, debug=False):
    c = a + b
    if debug:
        print("output: {}".format(c))
    return c
```
```
# Debug output disabled
>>>> sum(1, 2)
>>>> sum(1, 2, debug=False)
# Debug output enabled
>>>> sum(1, 2, debug=True)
[Out] output: 3
```

### How you would use debug now
```python
from quick_debug import quick_debug, logger

@quick_debug
def sum(a, b):  # No additional argument.
    c = a + b
    logger.DEBUG("output: {}".format(c))  # No if statement.
    return c
```
```
# Debug output disabled
>>>> sum(1, 2)
>>>> sum(1, 2, debug=False)
# Debug output enabled
>>>> sum(1, 2, debug=True)
[Out] output: 3
```
