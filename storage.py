class Stack(object):
    """Whitespace stack.
       Values are integers, with no maximum limitations.
       Use a list self.space to simulate a stack.
       self.space is free to access. But remember not to change the list
        when not necessary. The methods push() and pop() are for simplification.
    """

    def __init__(self, *args):
        """Use a series of values to initialize stack.
           In terms of safety, please ONLY initialize stack with integers.
        """
        self.space = []
        self.space += list(args)

    def push(self, value):
        """Push a value to stack.
           The method will check whether the value is an integer or a string
           If given an integer, the value will be directly pushed.
           Else if given a string, the first character of that string will be
            converted into it's ASCII code, and then be pushed.
        """
        try:
            if isinstance(value, int):
                self.space.append(value)
            else:
                # value is str?
                self.space.append(ord(value[0]))
        except TypeError:
            print("Stack only accept an integer or a character.")

    def pop(self):
        """Pop stack. Will return the popped one.
           If stack is empty, will print an error message.
        """
        try:
            return self.space.pop()
        except IndexError:
            print("Empty stack cannot pop.")


class Heaps(object):
    """Whitespace heap storage.
       Heap storage is a set of random accessible registers. Each of the heap
        is given an address like bytes on RAM, and can store one integer with
        no value limitations.
       The size of heap storage is unlimited. The storage is simulated by a
        dictionary where heap address are keys, stored numbers are values.
    """

    def __init__(self):
        self.storage = {}

    def set_heap(self, address, value):
        """Open up or rewrite a heap space.
           Heap storage will append a new key-value pair of { address: value }.
           Both address and value are required to be an integer. Expressly,
            address should be unsigned. If given a negative address, it will
            be automatically converted into its absolute value.
        """
        if isinstance(address, int):
            if address < 0:
                address = -address
            try:
                if isinstance(value, int):
                    pass
                else:
                    # value is str?
                    value = ord(value[0])
            except TypeError:
                print("Heap can only store an integer or a character.")

            self.storage[address] = value
        else:
            print("Invalid heap address.")

    def del_heap(self, address):
        """Delete heap storage at the given address.
           Will print an error message if deleting a null heap.
        """
        try:
            self.storage.pop(address)
        except KeyError:
            print("Storage at the given address doesn't have value.")
