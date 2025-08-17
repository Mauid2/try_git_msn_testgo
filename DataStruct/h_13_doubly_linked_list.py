# 创建节点类：包含数据、前驱节点和后继节点
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

# 创建双向链表，只需要给定头结点即可
class Double_linked_list:
    def __init__(self):
        self.head=None

    def add_node(self,data):
        new_node=Node(data)
        new_node.next=self.head
        if self.head:
            self.head.prev=new_node
        self.head=new_node

    def print_node(self):
        current=self.head
        if current is None:
            print("Empty List")
        while current:
            print(current.data)
            current=current.next

    def insert_node(self,prev_node,data):
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        new_node.next.prev=new_node


dlist=Double_linked_list()
dlist.add_node(1)
dlist.add_node(2)
dlist.add_node(3)

dlist.insert_node(dlist.head.next,4)
dlist.print_node()
