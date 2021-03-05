#  --------------------------------------------------------------------------
#  Copyright (c) 2021, antuit.ai. All rights reserved.
#  Proprietary and confidential
#  Unauthorized copying of this file, via any medium, is strictly prohibited.
#  --------------------------------------------------------------------------


from functools import partial


class pipe:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if kwargs and not args:
            return pipe(partial(self.func, **kwargs))
        return self.func(*args, **kwargs)

    def __rrshift__(self, other):
        return self.func(other)

    def __rshift__(self, other):
        return other.__rrshift__(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.func.__name__})"

