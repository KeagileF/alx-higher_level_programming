#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Function is executed safely.

    Args:
        fct: Function to be executed.
        args: Arguments for fct.

    Returns:
        If error occurs - None.
        Otherwise - Result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
