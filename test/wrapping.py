class A:
        def __init__(self, val, fn):
                self.val = val
                self.fn  = fn

        def call(self):
                self.fn()



class B(A):
        def __init__(self, value):
                super().__init__(value, self.greet)

        def greet(self):
                print("Namaste")



def hi():
        print("Hi")

        
obj = B(5)
