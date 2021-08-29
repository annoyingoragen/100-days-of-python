import math
def cans(height, width, coverage):
    numberofcans=math.ceil(height*width)/5
    print(f"you will need {numberofcans} cans")


test_h=int(input("HEIGHT OF WALL: "))
test_w=int(input("WIDTH OF WALL: "))
cover=5


cans(width=test_w,height=test_h,coverage=cover)