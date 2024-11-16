## PYRAMID ###
#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
for i in range(1,5):
    for j in range(4-i):
        print(" ",end=" ")
    for k in range(1,i*2):
        print("*",end=" ")
    print()



### NUMBER PYRAMID ###
#     1 
#   2 3 4 
# 5 6 7 8 9 
k=1
for i in range(1,4):
    for j in range(3-i):
        print(" ",end=" ")
    for j in range(1,i*2):
        print(k,end=" ")
        k+=1
    print()





## DIAMOND ###
#       * 
#     * * * 
#   * * * * * 
# * * * * * * * 
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 
for i in range(1,5):
    for j in range(4-i):
        print(" ",end=" ")
    for j in range(1,i*2):
        print("*",end=" ")
    print()
for k in range(4,0,-1):
    for j in range(4-k):
        print(" ",end=" ")
    for j in range(2*k-1):
        print("*",end=" ")
    print()


## HOLLOW SQUARE ###
# * * * * 
# *     * 
# *     * 
# * * * * 
for i in range(1,5):
    for j in range(1,5):
        if(i==1 or i==4 or j==1 or j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

