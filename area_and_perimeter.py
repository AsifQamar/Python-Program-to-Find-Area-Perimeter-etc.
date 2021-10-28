print("************************************************ Enter a Choice **********************************************")
print("1)Square\n2)Rectangle\n3)Circle\n4)Triangle")
choice = input("Your Choice - ")
if choice=="1" or choice=="Square" or choice=="square":
    choice2 = input("Do you want Perimeter(p) or Area(a)?\n")
    side = float(input("Enter Side of the Square: "))
    if choice2 == "Perimeter" or choice2=="perimeter" or choice2=="p":
        peri_square=4*side
        print("The Primeter of your Square is",peri_square)
    if choice2 == "Area" or choice2=="area" or choice2=="a":
        area_square = side**2
        print("The Area of your Square is",area_square)
if choice=="2" or choice=="Rectangle" or choice=="rectangle":
    choice2 = input("Do you want Perimeter(p) or Area(a)?\n")
    length = float(input("Enter Lentgth of the Rectangle: "))
    breadth = float(input("Enter Breadth of the Rectangle: "))
    if choice2 == "Perimeter" or choice2=="perimeter" or choice2=="p":
        peri_rect=2*(length+breadth)
        print("The Perimeter of your Rectangle is",peri_rect)
    if choice2 == "Area" or choice2=="area" or choice2=="a":
        area_rect = length*breadth
        print("The Area of your Rectangle is",area_rect)
if choice=="3" or choice=="Circle" or choice=="circle":
    choice2 = input("Do you want Circumfrance(c) or Area(a)?\n")
    radius = float(input("Enter Radius of the Rectangle: "))
    pi = 3.14
    if choice2 == "Circumfrance" or choice2=="circumfrance" or choice2=="c":
        circum_circle=2*pi*radius
        print("The Circumfrance of your Circle is",circum_circle)
    if choice2 == "Area" or choice2=="area" or choice2 == "a":
        area_circle = pi*radius**2
        print("The Area of your Circle is",area_circle)
if choice=="4" or choice=="Triangle" or choice=="triangle":
    choice2 = input("Do you want Perimeter(p) or Area(a)?\n")
    if choice2 == "Perimeter" or choice2=="perimeter" or choice2=="p":
        tri_side1 = float(input("Enter First side of the Triangle: "))
        tri_side2 = float(input("Enter Second side of the Triangle: "))
        tri_side3 = float(input("Enter Third side of the Triangle: "))
        peri_tri=tri_side3+tri_side1+tri_side2
        print("The Perimeter of your Triangle is",peri_tri)
    if choice2 == "Area" or choice2=="area" or choice2=="a":
        height = float(input("Enter Height of the Triangle: "))
        base = float(input("Enter Base of the Triangle: "))
        area_tri = height*base*1/2
        print("The Area of your Triangle is",area_tri)