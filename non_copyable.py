class NonCopyable:
    def __copy__(self):
        raise TypeError(f"{type(self).__name__} nie mozna skopiowac")

    def __deepcopy__(self, memo):
        raise TypeError(f"{type(self).__name__} nie mozna skopiowac")
