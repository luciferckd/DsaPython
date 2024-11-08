# # array is a data sturcture is used each array element and comes array index which using

# array = [10, 20, 30, 40, 50]


# print(array[2])
# # update element
# array[2] = 34

# print(array)

# # linked list data structure







class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new

    def comes(self):
        curr = self.head
        while curr:
            print(curr.data, end='....')
            curr = curr.next
        print("semma po da")


l1 = linkedlist()
l1.append(23)
l1.append(25)

l1.comes()
    
