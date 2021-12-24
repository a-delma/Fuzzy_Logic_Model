from functools import partial

class Infix(object):
    """ Allows for the creation of infix operations 
    
        Done to make boolean evaluation a bit easier
    """
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def feq(left,right):
    """ Infix trinary equality """
    args = [left, right]
    if 1 in args:
        if 0 in args:
            return False
        else:
            return True
    elif 0 in args:
        if 2 in args:
            return False
    return True