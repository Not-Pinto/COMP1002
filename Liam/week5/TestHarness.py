from DSALinkedList import DSALinkedList
from DSAStack import DSAStack
from DSAQueue import DSAQueue

def linked_list_test():
    print("\nTest for linked list\n")
    linked_list = DSALinkedList()
    
    print("Checking is_empty mehtod, expected True:", linked_list.is_empty())
    print("Checking list_length mehtod, expected 0:", linked_list.list_length())

    print("Adding 10 to start of the list")
    linked_list.insert_first(10)
    print("Adding 20 to start of the list")
    linked_list.insert_first(20)
    print("Adding 30 to end of the list")
    linked_list.insert_last(30)

    print("Checking is empty_mehtod and insert methods expected, False:", linked_list.is_empty())
    print("Checking list_length mehtod and insert methods, expected 3:", linked_list.list_length())

    print("Checking peek_first and insert_first methods, expected 20:", linked_list.peek_first())
    print("Checking peek_last mehtod and insert_last, expected 30:", linked_list.peek_last())

    print("Cheking remove_first method, expected 20:", linked_list.remove_first())
    print("Confirming with peek_first, expected 10:", linked_list.peek_first())
    print("Confriming with list_length, expected 2:", linked_list.list_length())

    print("Cheking remove_last method, expected 30:", linked_list.remove_last())
    print("Confirming with peek_last, expected 10:", linked_list.peek_first())
    print("Confriming with list_length expected 1:", linked_list.list_length())

    print("removing last item in the list")
    linked_list.remove_last()
    print("confirm list is empty, expected True:", linked_list.is_empty())

    print("Checking error handling, (trying to remove when list is empty)")
    print("Should raise Runtime: list is empty error")
    try:
        linked_list.remove_last()
    except RuntimeError:
        print("Error recived corectly")

    print("End of Linked List test")
    


def stack_test():
    print("\nTest for stack\n")
    stack = DSAStack()

    print("Checking is_empty mehtod, expected True:", stack.is_empty())
    print("Checking get_count mehtod, expected 0:", stack.get_count())

    print("Pushing 10 to the stack")
    stack.push(10)
    print("Pushing 20 to the stack")
    stack.push(20)
    print("Pushing 30 to the stack")
    stack.push(30)

    print("Checking is_empty and push mehtods, expected False:", stack.is_empty())
    print("Checking get_count and push mehtods, expected 3:", stack.get_count())

    print("Checking the top method, expected 30:", stack.top())
    print("Checking the pop mehtod, expected 30:", stack.pop())
    print("Confirming with get_count method, expected 2:", stack.get_count())
    print("Confirming with top method, expected 20:", stack.top())

    print("Poping item, expected 20:", stack.pop())
    print("Poping last item, expected 10:", stack.pop())
    print("Checking the stack is empty, expected True:", stack.is_empty())

    print("Checking error handling")

    print("Attempting to run top method on empty stack")
    print("Should recive a RuntimeError: stack is empty")
    try:
        stack.top()
    except RuntimeError:
        print("Error recived corectly")

    print("Attempting to run pop method on empty stack")
    print("Should recive a RuntimeError: stack is empty")
    try:
        stack.top()
    except RuntimeError:
        print("Error recived corectly")

    print("End of stack test")



def queue_test():
    print("\nTest for queue\n")
    queue = DSAQueue()

    print("Checking is_empty mehtod, expected True:", queue.is_empty())
    print("Checking get_count mehtod, expected 0:", queue.get_count())

    print("Enqueing 10 to the queue")
    queue.enqueue(10)
    print("Enqueing 20 to the queue")
    queue.enqueue(20)
    print("Enqueing 30 to the queue")
    queue.enqueue(30)

    print("Checking is_empty and push mehtods, expected False:", queue.is_empty())
    print("Checking get_count and push mehtods, expected 3:", queue.get_count())

    print("Checking the peek method, expected 10:", queue.peek())
    print("Checking the dequeue mehtod, expected 10:", queue.dequeue())
    print("Confirming with get_count method, expected 2:", queue.get_count())
    print("Confirming with peek method, expected 20:", queue.peek())

    print("Dequeing item, expected 20:", queue.dequeue())
    print("Dequeing last item, expected 10:", queue.dequeue())
    print("Checking the queue is empty, expected True:", queue.is_empty())

    print("Checking error handling")

    print("Attempting to run peek method on empty queue")
    print("Should recive a RuntimeError: Queue is empty")
    try:
        queue.peek()
    except RuntimeError:
        print("Error recived corectly")

    print("Attempting to dequeue method on empty queue")
    print("Should recive a RuntimeError: queue is empty")
    try:
        queue.dequeue()
    except RuntimeError:
        print("Error recived corectly")

    print("End of queue test")



selection1 = None
print("Do you want to test DSALinkedList(1), DSAStack(2), DSAQueue(3)")
while selection1 == None:
    try: 
        selection1 = int(input("Please enter 1, 2, 3: "))
        if 1 > selection1 or selection1 > 3:
            print("\nOut of range")
            selection1 = None
    except ValueError: 
         print("\nIntigers only")

if selection1 == 1:
    linked_list_test()
elif selection1 == 2:
    stack_test()
else:
    queue_test()