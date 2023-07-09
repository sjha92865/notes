# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print('Welcome to Coding Ninjas Studio Online Compiler!!')
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.nextt=None

class DBLL:
    def __init__(self):
        self.head=None
    def insert_at_front(self,data):
        new_node=Node(data)
        new_node.nextt=self.head
        if self.head!=None:
            self.head.prev=new_node
            self.head=new_node
        else:
            self.head=new_node
    def addNode(self,data):#add node at last
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        # print(self.head)
        else:
            curr=self.head
            while curr.nextt!=None:
                curr=curr.nextt
            # new_node.prev=self.head
            # self.head.nextt=new_node
            new_node.prev=curr
            curr.nextt=new_node

            
        
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.data);    
            current = current.nextt; 

dList = DBLL();    
#Add nodes to the list    
dList.addNode(1);    
dList.addNode(2);    
dList.insert_at_front(3);    
dList.addNode(4);    
# dList.addNode(5);    
     
#Displays the nodes present in the list    
dList.display();     
