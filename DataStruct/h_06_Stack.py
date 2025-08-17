class Stack:
   def __init__(self):
      self.stack = []

   # 添加元素
   def add(self, dataval):
      if dataval not in self.stack:
         self.stack.append(dataval)
         return True
      else:
         return False

   # 获取栈顶元素
   def peek(self):
	   return self.stack[-1]

   # 移除栈顶元素
   def remove(self):
       if len(self.stack)==0:
           return "Stack is empty"
       else:
           return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())
print(AStack.remove())
