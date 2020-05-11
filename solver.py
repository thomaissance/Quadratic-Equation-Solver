from cmath import sqrt

def quadratic_formula(a, b, c):
    a=float(a)
    b=float(b)
    c=float(c)
    if (b**2)-4*a*c>=0:
        print ("X= ", (-b+sqrt((b**2)-4*a*c))/(2*a))
        print ("X= ", (-b-sqrt((b**2)-4*a*c))/(2*a))
    else:
     print ("no real roots")

if __name__ == "__main__":
     while True:
         print( "ax^2+bx+c=0" )
         a = input("a= ")
         b = input("b= ")
         c = input("c= ")
         solution = quadratic_formula(a, b, c) 
         print(solution)
         if "they don't want to continue":
             break
