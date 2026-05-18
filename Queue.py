#Queue DS:-
#1.Enqueue
#2.Dequeue
#3.display queue
#4.isEmpty()
#5.isFull()
#6.Delete
#8.

import sys
class Queue:
    def __init__(self,size):
        self.myQueue=[]
        self.queueSize=size
    def isFull(self):
        if len(self.myQueue)==size:
            return True
        else:
             return False
    def enQueue(self,value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.myQueue.append(value)

    def display(self):
        print(self.myQueue)     

    def isEmpty(self):
        if self.myQueue ==[]:
            return True
        else:
            return False  

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.myQueue.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.myQueue[0])        
        
    def deleteQueue(self):
            self.myQueue =None


    
size = int(input("Enter the size of Queue:"))
obj = Queue(size)
print("Satck has craeted:")

while True:
    print("1.Enqueue operation:")
    print("2.Dispaly Queueu")
    print("3.Dequeue Operation:")
    print("4.peek operation:")
    print("5.Delete Operation:")
    print("6.exit")
    choice =int(input("Enter youe choice :"))
    if choice == 1:
        value = int(input("Enter elemnts to add in queue:"))
        obj.enQueue(value)

    elif choice ==2:
        obj.display()

    elif choice==3:
        obj.dequeue()

    elif choice==4:
        obj.peek()

    elif choice==5:
        obj.deleteQueue()

    elif choice==6:
        sys.exit()
        




