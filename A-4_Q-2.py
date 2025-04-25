import math

def count_sq_int(A , B):
    start = math.ceil(math.sqrt(A)) # ceiling value of x i.e., the smallest integer greater than or equal to x.
    end  = math.floor(math.sqrt(B)) #This function takes a floating-point number and returns the largest 
   # integer less than or equal to that number
    return max(0,end - start + 1)

T = int(input("Enter number of test cases you want! \n"))
for i in range(T):
    # A = int(input())
    # B = int(input())
    A , B = map(int,input().split())
    print(count_sq_int(A,B))
    