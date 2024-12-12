class Simple:
    def __init__(self, param):
        self.param = param

    def print(self):
        print('The parameter is {}.'.format(self.param))

simple = Simple(10)
simple.print()
