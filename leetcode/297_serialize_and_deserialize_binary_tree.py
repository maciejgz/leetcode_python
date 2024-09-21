


from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.val)
        
        
class Codec:

    def serialize(self, root) -> str:
        if root is None:
            return "None"
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        
        return ','.join(result)
        
        

    def deserialize(self, data):
        if data == "None":
            return None
        
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        index = 1
        
        while queue:
            node = queue.popleft()
            if nodes[index] != "None":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            if nodes[index] != "None":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        
        return root
        
        
if __name__ == "__main__":
    ser = Codec()
    deser = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    seerialized = ser.serialize(root);
    print("serialized: ", seerialized)
    ans = deser.deserialize(seerialized)
    print(ans)