import unittest
import random

class Node(object):
    def __init__(self, val, double_link=False):
        self.val = val
        self.next = None
        if double_link:
            self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def empty(self):
        self.head = None
        self.tail = None
        return self

    def length(self):
        if self.isEmpty():
            return 0
        cursor = self.head
        count = 0
        while(cursor != None):
            count += 1
            cursor = cursor.next
        return count

    def toList(self):
        a = []
        cursor = self.head
        while(cursor != None):
            a.append(cursor.val)
            cursor = cursor.next
        return a

    def insert_head(self, val):
        if self.isEmpty():
            n = Node(val)
            self.head = n
            self.tail = n
        else:
            n = Node(val)
            n.next = self.head
            self.head = n
        return self

    def insert_tail(self, val):
        if self.isEmpty():
            n = Node(val)
            self.head = n
            self.tail = n
        else:
            n = Node(val)
            self.tail.next = n
            self.tail = n
        return self

    def remove_head(self):
        if self.isEmpty():
            raise Exception('Error: cannot remove from empty list')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            n = self.head
            new_head = n.next
            self.head = new_head
        return self

    def remove_tail(self):
        if self.isEmpty():
            raise Exception('Error: cannot remove from empty list')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            cursor = self.head
            while (cursor.next != self.tail):
                cursor = cursor.next
            self.tail = cursor
            self.tail.next = None
        return self

    def remove_value(self, val):
        """A slightly rough remove value function. I assume we are
            only removing a single node and that there are no duplicate
            values
        """
        cursor = self.head
        while(cursor != None):
            if cursor.val == val:
                # found the node we need to remove, do stuff here
                if cursor == self.head:
                    return self.remove_head()
                elif cursor == self.tail:
                    return self.remove_tail()
                else:
                    # we are removing a node from some place in the middle of the list.
                    # this means we are guaranteed to have a node coming after the
                    # cursor
                    cursor.val = cursor.next.val
                    cursor.next = cursor.next.next
                    if cursor.next == None:
                        self.tail = cursor
                    return self
            cursor = cursor.next
        # loop ends here and that means we didn't find anything. You can handle this with
        # an exception if you like or just let it ride
        else:
            raise Exception('value not found')

class Stack(LinkedList):

    def push(self, val):
        return self.insert_tail(val)

    def pop(self):
        return self.remove_tail()

class Queue(LinkedList):

    def enque(self, val): 
        return self.insert_tail(val)

    def dequeu(self): 
        return self.remove_head()

class TestQueu(unittest.TestCase):

    def setUp(self):
        self.Queue = Queue()

    def test_enqueu(self):
        self.Queue.insert_head(5)
        self.Queue.insert_head(4)
        self.Queue.insert_head(3)
        self.Queue.insert_head(2)
        self.Queue.insert_head(1)

        self.Queue.enque(10)
        self.assertEqual(self.Queue.toList(), [1,2,3,4,5,10])

        # multiple enque
        self.Queue.enque(11)
        self.Queue.enque(12)
        self.Queue.enque(13)
        self.assertEqual(self.Queue.toList(), [1,2,3,4,5,10,11,12,13])
        

    def test_dequeu(self):
        self.Queue.insert_head(5)
        self.Queue.insert_head(4)
        self.Queue.insert_head(3)
        self.Queue.insert_head(2)
        self.Queue.insert_head(1)

        self.Queue.dequeu()
        self.assertEqual(self.Queue.toList(), [2,3,4,5])

        #multiple deque
        self.Queue.dequeu()
        self.Queue.dequeu()
        self.assertEqual(self.Queue.toList(), [4,5])

        self.Queue.dequeu()
        self.Queue.dequeu()
        self.assertEqual(self.Queue.toList(), [])




class TestStack(unittest.TestCase):
    def setUp(self):
        self.Stack = Stack()

    def test_push(self):
        self.Stack.insert_head(5)
        self.Stack.insert_head(4)
        self.Stack.insert_head(3)
        self.Stack.insert_head(2)
        self.Stack.insert_head(1)

        # [1,2,3,4,5]
        self.Stack.toList() 
        self.Stack.push(10)
        self.assertEqual(self.Stack.length(), 6)
        self.assertEqual(self.Stack.toList(), [1,2,3,4,5,10])

        # multiple push
        self.Stack.push(11)
        self.Stack.push(12)
        self.Stack.push(13)
        self.assertEqual(self.Stack.length(), 9)
        self.assertEqual(self.Stack.toList(), [1,2,3,4,5,10,11,12,13])


    def test_pop(self):
        self.Stack.insert_head(5)
        self.Stack.insert_head(4)
        self.Stack.insert_head(3)
        self.Stack.insert_head(2)
        self.Stack.insert_head(1)

        # [1,2,3,4,5]
        self.Stack.toList() 
        self.Stack.pop()
        self.assertEqual(self.Stack.length(), 4)
        self.assertEqual(self.Stack.toList(), [1,2,3,4])

        # multiple pop => empty
        self.Stack.pop()
        self.Stack.pop()
        self.Stack.pop()
        self.Stack.pop()
        self.assertEqual(self.Stack.length(), 0)
        self.assertEqual(self.Stack.toList(), [])


class TestLists(unittest.TestCase):

    def setUp(self):
        self.LL = LinkedList()

    def test_remove_value(self):
        self.LL.insert_head(5)
        self.LL.insert_head(4)
        self.LL.insert_head(3)
        self.LL.insert_head(2)
        self.LL.insert_head(1)
        
        self.LL.remove_value(3)
        self.assertEqual(self.LL.length(), 4)
        self.assertEqual(self.LL.toList(), [1, 2, 4,5])

    def test_remove_value_empty(self):
        self.LL.empty()
        with self.assertRaises(Exception) as e:
            self.LL.remove_value(3)

    def test_remove_value_single(self):
        self.LL.insert_tail(5)
        self.LL.remove_value(5)
        self.assertEqual(self.LL.toList(), [])

    def test_remove_value_not_found(self):
        self.LL.insert_head(5)
        self.LL.insert_head(4)
        self.LL.insert_head(3)
        self.LL.insert_head(2)
        self.LL.insert_head(1)
        
        with self.assertRaises(Exception) as e:
            self.LL.remove_value(6)


    def test_list_length(self):
        for j in range(20):
            self.LL.empty()
            tries = random.randrange(0, 100)
            for i in range(tries):
                self.LL.insert_head(4)
            self.assertEqual(tries, self.LL.length())

    def test_to_list(self):
        self.LL.insert_head(4)
        self.LL.insert_head(3)
        self.LL.insert_head(2)
        self.LL.insert_head(1)
        self.assertEqual(
            [1,2,3,4],
            self.LL.toList()
            )

    def test_insert_head_empty(self):
        self.LL.insert_head(2)
        self.assertEqual(self.LL.head.val, 2)
        self.assertEqual(self.LL.tail.val, 2)
        self.assertEqual(self.LL.length(), 1)
        
    def test_insert_head_non_empty(self):
        self.LL.insert_head(2)
        self.LL.insert_head(3)
        self.assertEqual(self.LL.head.val, 3)
        self.assertEqual(self.LL.tail.val, 2)
        self.assertEqual(self.LL.length(), 2)

    def test_insert_head_many(self):
        for j in range(20):
            self.LL.empty()
            rand_array = [random.randrange(0,10000) for i in xrange(100)]
            for x in rand_array:
                self.LL.insert_head(x)

            rand_array_reverse = rand_array[::-1]
            self.assertEqual(
                rand_array_reverse,
                self.LL.toList())

    def test_insert_tail_empty(self):
        self.LL.insert_tail(5)

        self.assertEqual(self.LL.tail.val, 5)
        self.assertEqual(self.LL.head.val, 5)
        self.assertEqual(self.LL.length(), 1)
        
    def test_insert_tail_non_empty(self):
        self.LL.insert_head(3)
        self.LL.insert_tail(5)

        self.assertEqual(self.LL.head.val, 3)
        self.assertEqual(self.LL.tail.val, 5)
        self.assertEqual(self.LL.length(), 2)

    def test_insert_tail_many(self):
        for j in range(20):
            self.LL.empty()
            rand_array = [random.randrange(0,10000) for i in xrange(100)]
            for x in rand_array:
                self.LL.insert_tail(x)

            self.assertEqual(
                rand_array,
                self.LL.toList())    

    def test_remove_head(self):
        self.LL.insert_head(4)
        self.LL.insert_head(3)
        self.LL.insert_head(2)
        self.LL.insert_head(1)
        self.assertEqual(self.LL.length(), 4)
        self.assertEqual(self.LL.head.val, 1)

        self.LL.remove_head()
        self.assertEqual(self.LL.length(), 3)
        self.assertEqual(self.LL.head.val, 2)

    def test_remove_head_empty(self):
        self.LL.empty()
        with self.assertRaises(Exception) as e:
            self.LL.remove_head()

    def test_remove_tail_empty(self):
        self.LL.empty()
        with self.assertRaises(Exception) as e:
            self.LL.remove_tail()

    def test_remove_head_single(self):
        self.LL.empty()
        self.LL.insert_head(5)
        self.LL.remove_head()

        self.assertEqual(self.LL.length(), 0)
        self.assertEqual(self.LL.head, None)
        self.assertEqual(self.LL.tail, None)

    def test_remove_tail(self):
        self.LL.insert_head(3)
        self.LL.insert_head(2)
        self.LL.insert_head(1)
        self.LL.insert_tail(4)
        self.assertEqual(self.LL.length(), 4)
        self.assertEqual(self.LL.head.val, 1)

        self.LL.remove_tail()
        self.assertEqual(self.LL.length(), 3)
        self.assertEqual(self.LL.tail.val, 3)

    def test_remove_tail_single(self):
        self.LL.empty()
        self.LL.insert_tail(1)
        self.LL.remove_tail()

        self.assertEqual(self.LL.head, None)
        self.assertEqual(self.LL.tail, None)
        self.assertEqual(self.LL.length(), 0)


if __name__ == '__main__':
    unittest.main()
