"""
Objective
Today, we're working with Binary Search Trees (BSTs). Check out the Tutorial tab for learning materials and an instructional video!

Task
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf. You are given a pointer, root,
pointing to the root of a binary search tree. Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.

Input Format

The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
The first line contains an integer, n, denoting the number of nodes in the tree.
Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added to the BST.

Output Format

The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of the BST.

Sample Input

7
3
5
2
1
4
6
7

Sample Output

3

"""


#Solution

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        maxHeight = [0]
        self.getHeightRec(root,0,maxHeight)
        return maxHeight[0]

    def isLeaf(self,currentNode):
        return currentNode.left is None and currentNode.right is None


    def getHeightRec(self, currentNode, currentHeight, maxHeight):
        if currentNode is None:
            return

        if self.isLeaf(currentNode):
            if currentHeight > maxHeight[0]:
                maxHeight[0] = currentHeight

            return

        if currentNode.left is not None:
            self.getHeightRec(currentNode.left, currentHeight + 1, maxHeight)

        if currentNode.right is not None:
            self.getHeightRec(currentNode.right, currentHeight + 1, maxHeight)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
