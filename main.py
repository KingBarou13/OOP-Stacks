class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stackArray = [None] * max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Queue is already full")
        self.top += 1
        self.stackArray[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Queue is already empty")
        item = self.stackArray[self.top]
        self.stackArray[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is already empty")
        return self.stackArray[self.top]

    def size(self):
        return self.top + 1


def mulBase(num, base):
    s = Stack(10)
    while num > 0:
        s.push(num % base)
        num //= base
    converted = ""
    while not s.is_empty():
        converted += str(s.pop())
    return converted

size = int(input("Enter the size of the stack: "))
stack = Stack(size)

while True:
    print("\nChoose an option:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check Size")
    print("5. Base Conversion")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to push: ")
        stack.push(item)
    elif choice == 2:
        popped_item = stack.pop()
        if popped_item is not None:
            print("Popped item:",popped_item)
    elif choice == 3:
        top_item = stack.peek()
        if top_item is not None:
            print("Top item:", top_item)
    elif choice == 4:
        print("Stack size:", stack.size())
    elif choice == 5:
        num = int(input("Enter the number: "))
        base = int(input("Enter the base: "))
        result = mulBase(num, base)
        print(f"{num} in base {base} is: {result}")
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

