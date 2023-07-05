# Statement

Given the **root** of a binary tree, the task is to flatten the tree into a linked list using the same TreeNode class. The left child pointer of each node in the linked list should always be NULL, and the right child pointer should point to the next node in the linked list. The nodes in the linked list should be in the same order as that of the preorder traversal of the given binary tree.

## Constraints:

    −100≤−100≤ Node.data ≤100≤100.
    The tree contains nodes in the range [1,500][1,500].

# Solution

So far, you’ve probably brainstormed some approaches and have an idea of how to solve this problem. Let’s explore some of these approaches and figure out which one to follow based on considerations such as time complexity and any implementation constraints.

## Naive approach

The naive approach to flatten a binary tree into a linked list is to perform a preorder traversal of the tree and store the visited nodes in a Queue. After the traversal, start dequeuing the nodes and set the pointers of each node such that: the right pointer of the dequeued node is set to the previously dequeued node, and the left pointer is set to NULL.

However, this naive approach requires extra memory because it uses a Queue. The space complexity would be O(n)O(n). However, can the problem be solved without additional data structures?

## Optimized approach using depth-first search

To flatten the binary tree, we will follow a **depth-first search** approach. We start at the root node and for each node and find the right-most node in its left subtree. We set the right pointer of the right-most node to the current node’s right pointer. After that, we set the current node’s right pointer to the current node’s left pointer. Finally, we set the current node’s left pointer to NULL. We will repeat this process for all nodes in the binary tree.

# Solution summary

- Traverse the binary tree, and for each node, check if it has a left child.
- If the left child exists, find the rightmost node in the left subtree.
- Point the right pointer of the rightmost node to the right child of the current node.
- Set the current node’s right pointer to the current node’s left pointer.
- Set the current node’s left child to NULL.
- Repeat the steps above until the entire binary tree has been traversed.
