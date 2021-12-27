class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # not having tail pointer would function similarly
        # but only appending item to the list is O(n)
        # because you have to traverse the whole list to get to the end

    def isHead(self, node):
        return(node == self.head)

    def isTail(self, node):
        return(node == self.tail)

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Double linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_with_info(self):
        if self.head is None:
            print("Double linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            if self.isHead(itr):
                llstr += '(head) '
            if self.isTail(itr):
                llstr += '(tail) '
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        if self.tail is None:
            print("Double linked list is empty")
            return
        itr = self.tail
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <-- ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.get_length() == 0:          # Same as self.head == None
            node = Node(data)
            self.head = node
            self.tail = node
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.get_length() == 0:          # Same as self.head == None
            self.insert_at_beginning(data)
        else:
            node = Node(data, None, self.tail)
            self.tail.next = node
            self.tail = node

    def insert_at(self, index, data):
        # index doesn't match
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        # insert at head
        if index == 0:
            self.insert_at_beginning(data)
            return
        # other cases
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                if self.isTail(itr):
                    self.tail = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        len = self.get_length()
        # index doesn't match
        if index < 0 or index >= len:
            raise Exception("Invalid Index")
        # remove head
        if index == 0:
            if self.isTail(self.head):
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        # remove tail
        if index == len - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        # other cases
        itr = self.head
        count = 0
        while itr.next:
            if count == index - 1:
                if self.isTail(itr.next):
                    itr.next.next = None
                else:
                    itr.next.next.prev = itr
                    itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                if self.isHead(itr):
                    if self.isTail(itr):
                        self.head = None
                        self.tail = None
                    else:
                        self.head = itr.next
                        self.head.prev = None
                elif self.isTail(itr):
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    itr.prev.next = itr.next
                    itr.next.prev = itr.prev
                break
            itr = itr.next


if __name__ == '__main__':
    '''
    ll = DoubleLinkedList()
    ll.insert_values([45, 7, 12, 567, 99])
    ll.remove_by_value(99)
    ll.print_forward()
    '''
    ll = DoubleLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_with_info()
    ll.insert_at(0, "jackfruit")
    ll.print_with_info()
    ll.insert_at(6, "dates")    # this is where tail got messed up
    ll.print_with_info()
    ll.insert_at(2, "kiwi")
    ll.print_with_info()
    print("--------------------------")
    ll.remove_at(0)
    ll.print_with_info()
    ll.remove_at(ll.get_length()-1)
    ll.print_with_info()
    ll.remove_at(3)
    ll.print_with_info()
