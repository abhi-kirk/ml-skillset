class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for curr_node in self:
            if curr_node.next is None:
                curr_node.next = node
                node.next = None

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Node with data {target_node_data} not found")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        if self.head == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                new_node.next = node
                prev_node.next = new_node
                return 
            prev_node = node
        raise Exception(f"Node with data {target_node_data} not found")

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = None
            return
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception(f"Node with data {target_node_data} not found")

    def get(self, i):
        if self.head is None:
            raise Exception("List is empty")
        if i<0:
            raise Exception("Invalid index")
        iter = 0
        for node in self:
            if iter==i:
                return node.data
            iter += 1
        if i>iter:
            raise Exception("Invalid index")

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Hack!
    def reverse(self):
        if self.head is None:
            return self
        l = []
        for node in self:
            l.append(node.data)
        l = l[::-1]
        return LinkedList(l)


    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
