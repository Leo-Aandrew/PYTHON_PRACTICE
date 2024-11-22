### SIMPLE USAGE OF CLASS AND OBJECT ###
### output: 11 ###
class A():
    def sum(self,a,b):
        c=a+b
        print(c)

obj=A()
obj.sum(2,9)


### linkedlist ###
### output: 1-->2-->3 ###
class linkedlist:
    def __init__(self,num):
        self.node=num
        self.next=None

ob1=linkedlist(1)
ob2=linkedlist(2)
ob3=linkedlist(3)
ob1.next=ob2
ob2.next=ob3

def printlist(head):
    current=head
    while current is not None:
        print(current.node,end="-->" if current.next else "\n")
        current=current.next

printlist(ob1)
