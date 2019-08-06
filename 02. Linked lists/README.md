# Chapter 2: Linked lists

A linked list is a data structure representing a sequence of nodes. In a single linked list, each node points to the next node in the linked list. A doubly linked list gives each node pointers to both the next node and the previous node.

Lookup time isn't constant because it needs to iterate through K elements, but adding or deleting has constant time.

## Creating a LinkedList

```java
class Node {
    Node next = null;
    int data;

    public Node(int d){
        data = d,
    }

    void appendToTail(int d){
        Node end = new Node(d);
        Node n = this;
        while (n.next != null){
            n = n.next
        }
        n.next = end;
    }
}

Node a = new Node(5);
Node b = new Node(7);
a.appendTotail(b);
```

We access the linked list through a reference to the head `Node` of the linked list. If multiple objects need a reference to the linked ilst, and then the head changes, some objects might reference the old head. We could implement a LinkedList class wrapping the Node class, and have a single member variable, the head Node. **LinkedLists can be singly linked or double linked** (linked from left to right or from right to left also).

## Deleting an element in a singly linked list

Given a node `n`, find the previous node `prev`, and set `prev.next = n.next`. Remember to check for null pointer and to update the head or tail pointer as necessary.

```java
Node deleteNode(Node head, int d){
    if (head == null) return null;
    Node n = head;

    if (n.data == d){
        return head.next; // moved head, if the node to be deleted is at head
    }

    while (n.next != null){
        if (n.next.data == d){
            n.next = n.next.next;
            return head; // head doesn't change
        }
        n = n.next; // iterate to the next node
    }
    return head;
}
```

## The runner technique

Sometimes two pointers are used, you iterate through the linked list with two pointers simultaneously, with one ahead of the other. The fast pointer might be ahead by a fixed amount, or hopping multiple nodes for each node that the 'slow' node iterates through.

If we have a linked list a1 -> a2 -> an -> b1 -> b2 -> bn and we want to rearrange it to a1 -> b1 -> a2 -> b2 ..., and we don't know how long the list is but we know its length is an even number, we could have one pointer p1 move every two elements for every one move that p2 does. When p1 reaches the end of the list, p2 will be at midpoint. Then, move p1 back to the front and on each iteration, p2 selects an element and inserts it after p1.

> Question: then why do we iterate to the end bzw midpoint of the list? Just start rearranging from the very beginning. But we need p2 to reach the end, still that can be done with just p2, no need to move p1 as well.

## Recursive problems

Many linked list problems rely on recursion. But remember that recursion techniques take O(n) space and they can be implemented iteratively, but they might be much more complex.

## Resources

* [Hackerrank string exercises](https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=linked-lists)
* [Java solutions](https://github.com/careercup/CtCI-6th-Edition/tree/master/Java/Ch%2002.%20Linked%20Lists)
* [C++ solutions](https://github.com/careercup/CtCI-6th-Edition-cpp/tree/a68ba3e1c630a4d218ff1294f3eaf5aeced449ec/chapter-2-Linked-Lists)
* [Python solutions](https://github.com/careercup/CtCI-6th-Edition-Python/tree/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter2)
