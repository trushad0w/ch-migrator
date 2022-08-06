class Singleton(type):
    """
    Metaclass which implements singleton logic
    """

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]

    def dispose(cls):
        cls.__instances.pop(cls, None)
