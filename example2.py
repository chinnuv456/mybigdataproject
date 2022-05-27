lass example:

    def __init__(self, max=0):

        self.max = max



    def __iter__(self):

        self.n = 1

        return self



    def __next__(self):

        if self.n <= self.max:

            result = self.n

            self.n += 1

            return result

    

            

numbers = example(6)

i = iter(numbers)

print(next(i))

print(next(i))

print(next(i))

print(next(i))

print(next(i))
