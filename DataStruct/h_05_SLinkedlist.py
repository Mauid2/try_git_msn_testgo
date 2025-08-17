class Node:
   def __init__(self, dataval):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   # 头插法
   def AtBegining(self, newdata):
      NewNode=Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      NewNode.nextval = self.headval
      self.headval = NewNode

   # 尾插法
   def AtEnd(self,newdata):
      NewNode=Node(newdata)
      if self.headval is None:
          NewNode=self.headval
          return
      last=self.headval
      while last.nextval:
         last=last.nextval
      last.nextval=NewNode

   # 中间插节点
   def InBetween(self,middle_node,newdata):
      NewNode=Node(newdata)
      if middle_node is None:
         print("The mentioned node is absent")
         return
      tmp=middle_node.nextval
      middle_node.nextval=NewNode
      NewNode.nextval=tmp

   # 删除节点
   def Remove(self, remove_key):
      head=self.headval
      if head is None:
         return
      if head.dataval==remove_key:
         self.headval=head.nextval
         return
      pre=head
      while pre.nextval is not None:
         if pre.nextval.dataval==remove_key:
            pre.nextval=pre.nextval.nextval
            break
         pre=pre.nextval
      if pre.nextval is None:
         print("Key not found in the list")


   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.AtBegining("Sun")
list.AtEnd("Thu")
list.InBetween(list.headval.nextval, "Fri")
list.Remove('Tue')
list.Remove('Summ')

list.listprint()