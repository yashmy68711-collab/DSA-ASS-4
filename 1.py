# dmmt_toolkit.py

# --- TASK 1: BINARY SEARCH TREE (BST) ---
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None: return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1 & 2: No child or one child
            if node.left is None: return node.right
            elif node.right is None: return node.left
            # Case 3: Two children
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.key)
            self.inorder_traversal(node.right, result)
        return result

# --- TASK 2: GRAPH (BFS/DFS) ---
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        self.adj_list[u].append((v, weight))

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        order = []
        while queue:
            u = queue.pop(0)
            order.append(u)
            for v, w in self.adj_list.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return order

    def dfs(self, start):
        visited = set()
        order = []
        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v, w in self.adj_list.get(u, []):
                if v not in visited:
                    _dfs(v)
        _dfs(start)
        return order

# --- TASK 3: HASH TABLE (SEPARATE CHAINING) ---
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key: return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx].pop(i)
                return True
        return False

# --- MAIN RUNNER ---
def main():
    print("--- TASK 1: BST TESTING ---")
    bst = BST()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for n in nums: bst.insert(n)
    print("Inorder (Initial):", bst.inorder_traversal(bst.root, []))
    print("Search 20:", bst.search(20), "| Search 90:", bst.search(90))
    
    bst.delete(20) # Leaf
    print("After delete 20 (Leaf):", bst.inorder_traversal(bst.root, []))
    bst.insert(65)
    bst.delete(60) # One child
    print("After delete 60 (One Child):", bst.inorder_traversal(bst.root, []))
    bst.delete(50) # Two children
    print("After delete 50 (Two Children):", bst.inorder_traversal(bst.root, []))

    print("\n--- TASK 2: GRAPH TESTING ---")
    g = Graph()
    edges = [('A','B',2), ('A','C',4), ('B','D',7), ('B','E',3), ('C','E',1), ('D','F',5), ('E','D',2), ('E','F',6), ('C','F',8)]
    for u, v, w in edges: g.add_edge(u, v, w)
    print("Adjacency List:", g.adj_list)
    print("BFS from A:", g.bfs('A'))
    print("DFS from A:", g.dfs('A'))

    print("\n--- TASK 3: HASH TABLE TESTING ---")
    ht = HashTable(5)
    keys = [10, 15, 20, 7, 12]
    for k in keys: ht.insert(k, f"Val_{k}")
    print("Table State (Collisions expected at index 0):", ht.table)
    print("Get 15:", ht.get(15), "| Get 7:", ht.get(7), "| Get 12:", ht.get(12))
    ht.delete(15)
    print("Bucket 0 after deleting 15:", ht.table[0])

if __name__ == "__main__":
    main()