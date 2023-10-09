class Node :
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def append_item(self,data):
        node =Node(data)
        if self.tail:
            self.tail.next=node
            self.tail=node
        else:
            self.head=node
            self.tail=node
        self.count +=1

    def iterate_item(self):
        current_item=self.head
        while current_item :
            val =current_item.data
            #print(val)
            current_item=current_item.next
            yield val

    def sereach_item(self,val):
        for x in self.iterate_item():
          if val == x :
                return True
        return False
    
    def length(self):
        return self.count
    
   
items=LinkedList() 
items.append_item(4)
items.append_item(6)
items.append_item(0)
items.append_item(7)

print("Length of the list is :",items.length())

for val in items.iterate_item():
    print(val)

if items.sereach_item(2):
    print("true")
else :
    print("False")

items.delete_item(7)

for val in items.iterate_item():
    print(val) 
# print(val)

