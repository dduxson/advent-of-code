class Node:
    def __init__(self, type, name, parent, size=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = size
        self.type = type
    
    def print(self, offset=0):
        node_str = '  ' * offset + '- ' + self.name + " (" + self.type
        if self.size != None:
            node_str += " size=" + str(self.size)
        node_str += ')'
        print(node_str)

        for child in self.children:
            child.print(offset + 1)

def ConstructTree():
    current_node = Node("dir", "/", None)
    top_node = current_node
    
    with open("./2022/7/input.txt", "r") as file:
        for line in file.readlines():
            line = line.strip('\n')

            if line.startswith("$ cd"):
                specified_name = line[5:]
                if specified_name == "..":
                    current_node = current_node.parent
                elif specified_name != "/" :
                    for child in current_node.children:
                        if child.name == specified_name:
                            current_node = child
                            continue
            
            elif not line.startswith("$ ls"):
                components = line.split(" ")
                if components[0] == "dir":
                    current_node.children.append(Node("dir", components[1], current_node))
                else:
                    current_node.children.append(Node("file", components[1], current_node, int(components[0])))

    return top_node

def FindAndPopulateDirectoriesSize(node):
    if node.type == "file":
        return node.size
    
    size = 0
    for child in node.children:
        size += FindAndPopulateDirectoriesSize(child)

    node.size = size
    return size

def SumDirSizesLessOrEqualMaxHelper(node, max_size, sum):
    if node.type != "dir":
        return
    if node.size <= max_size:
        sum[0] += node.size
    for child in node.children:
        SumDirSizesLessOrEqualMaxHelper(child, max_size, sum)

def SumDirSizesLessOrEqualMax(tree, max_size):
    sum = [0]
    SumDirSizesLessOrEqualMaxHelper(tree, max_size, sum)
    return sum[0]

def SmallestSizeDirGreaterOrEqualMinHelper(node, min_size, result_node):
    if node.type != "dir":
        return
    if node.size >= min_size and (len(result_node) == 0 or node.size < result_node[0].size):
        result_node.clear()
        result_node.append(node)
    for child in node.children:
        SmallestSizeDirGreaterOrEqualMinHelper(child, min_size, result_node)

def SmallestSizeDirGreaterOrEqualMin(tree, min_size):
    result_node = []
    SmallestSizeDirGreaterOrEqualMinHelper(tree, min_size, result_node)
    return result_node[0].size

def main():
    tree = ConstructTree()
    #tree.print()
    used_size = FindAndPopulateDirectoriesSize(tree)

    print(SumDirSizesLessOrEqualMax(tree, 100000))
    print(SmallestSizeDirGreaterOrEqualMin(tree, 30000000-(70000000-used_size)))

if __name__ == "__main__":
    main()