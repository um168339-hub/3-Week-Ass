class student:
    def __init__(self,name,mark1,mark2,mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        sum = mark1+mark2+mark3
        avg = sum/2
        print(avg)
std = student('Umar',68,80,75)