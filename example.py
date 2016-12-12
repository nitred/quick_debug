"""File containing an example for debug decorator."""
from quick_debug import quick_debug, logger


@quick_debug
def sum(a, b):
    """Simple function that returns a sum of two number."""
    c = a + b
    logger.debug("sum: {}".format(c))
    return c


sum(1, 1, debug=True)       # sum: 2 (enabled)
sum(1, 2, debug=False)      # sum: 3 (disabled, explicit)
sum(1, 3, debug=True)       # sum: 4 (enabled)
sum(1, 4)                   # sum: 5 (disabled, original function)
