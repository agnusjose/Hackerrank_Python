class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maxd=0
    def computeDifference(self ):
        self.maxd = abs(max(self.__elements) - min(self.__elements)) 
    @property
    def maximumDifference(self):
        return self.maxd
print("Enter the numbers in the array with a space between it: ")
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)