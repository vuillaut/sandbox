import os


def haunt(place='house'):
    print(f'The {place} now is haunted')

def pr_unblack_ghost():
    """
    This is submitted through PR to test black action
    """
    a = 13
    b = 3
    c = a + b
    print(c)
    print( "ho no, this is .................line.............................. is so very long ")

def another_unblack_function(a=0, b=1):
    """
        even bad docstring?
    """
    if (a == 0 or 
            b == 0 ):
        c = 1
    else:
        c = 0
    print(c)
    return c
        
    
def testing_flake8():
    a = 4
    print(a)
