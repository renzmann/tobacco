from functools import partial


class pipe:

    def __init__(self, func):
        self.func = func

    @property
    def __qualname__(self):
        return self.func.__qualname__

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

