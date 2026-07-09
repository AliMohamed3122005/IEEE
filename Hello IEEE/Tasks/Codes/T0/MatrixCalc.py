import numpy as np

def matinput():
    rows = int(input("Please Enter the number of rows: "))
    cols = int(input("Please Enter the number of columns: "))
    print("Please Enter the elements of the matrix row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))               #Take every elment after space and convert it to int and make alist of it and add this row to the matrix list
        matrix.append(row)
    return np.array(matrix)                                 #Convert the list of lists to a numpy array and return it
    


def matsum(arr1,arr2):
    z = arr1 + arr2
    print("The sum=\n",z)

def matsub(arr1,arr2):
    z = arr1 - arr2
    print("The sub=\n",z)

def matmull(arr1,arr2):
    z= np.matmul(arr1,arr2)
    print("The Mul=\n",z)

def scalarsum(arr1,arr2):
    print("Enter the scalar: ")
    scalar=int(input())
    z1=np.add(scalar,arr1)
    z2=np.add(scalar,arr2)
    print("The Scalar add 1=\n",z1)
    print("The Scalar add 2=\n",z2)

def scalarsub(arr1,arr2):
    print("Enter the scalar: ")
    scalar=int(input())
    z1=np.subtract(arr1,scalar)
    y1=np.subtract(scalar,arr1)
    z2=np.subtract(arr2,scalar)
    y2=np.subtract(scalar,arr2)
    print("The Scalar sub 1 (arr-scalar)=\n",z1)
    print("The Scalar sub 1 (scalar-arr)=\n",y1)
    print("The Scalar sub 2 (arr-scalar)=\n",z2)
    print("The Scalar sub 2 (scalar-arr)=\n",y2)

def matnorm(arr1,arr2):
    a_mean=arr1.mean()
    a_std=arr1.std()
    z=(arr1-a_mean)/a_std
    print("The norm 1 using Z-scope method\n",z)
    b_mean=arr2.mean()
    b_std=arr2.std()
    z=(arr2-b_mean)/b_std
    print("The norm 2 using Z-scope method\n",z)


def mainmenu(arr1,arr2):
    while True:
        print("Choose what you want to do:\n")
        print("1-Addition")
        print("2-subtraction")
        print("3-Multiplication")
        print("4-Scalar addition")
        print("5-Scalar subtraction")
        print("6-Normalization")
        print("7-Exit")

        choice = input("Choose an option: ")
        if choice == '7' :
            break
        
        if choice == '1' : matsum(arr1,arr2)
        elif choice == '2' : matsub(arr1,arr2)
        elif choice == '3' : matmull(arr1,arr2)
        elif choice == '4' : scalarsum(arr1,arr2)
        elif choice == '5' : scalarsub(arr1,arr2)
        elif choice == '6' : matnorm(arr1,arr2)
        else:
            print("Invalid choice")



arr1 = matinput()
arr2 = matinput()
mainmenu(arr1,arr2)


