# Chapter 3: Stacks and queues

## Implementing a stack

It uses LIFO (last in first out) ordering. Uses the following operations

* `pop()`: remove top item from stack
* `push(item)`: add item to top of stack
* `peek()`: return top of stack
* `isEmpty()`: true if and only if the stack is empty

Doesn't offer constant-time access to the `i`th item. But it allows constant-time additions and removals.

```java
public class MyStack<T> {
    private static class StackNode<T> {
        // attributes of nodes in the stack
        private T data;
        private StackNode<T> next;

        public StackNode(T data){
            this.data = data;
        }
    }

    // attribute of the stack
    private StackNode<T> top;

    public T pop() {
        if (top == null){
            throw new EmptyStackException();
        }
        T item = top.data;
        top = top.next;
        return item;
    }

    public void push(T item) {
        StackNode<T> t = new StackNode<T>(item);
        t.next = top;
        top = t;
    }

    public T peek() {
        if (top == null){
            throw new EmptyStackException();
        }
        return top.data;
    }

    public boolean isEmpty() {
        return top == null;
    }
}
```

Stacks can be useful in recursive algorithms when you need to push temporary data onto a stack as you recurse, but then remove as you backtrack. It can also be used to implement a recursive algorithm iteratively.

## Implementing a queue

A queue implements FIFO (first in, first out) ordering. Items are removed from the queue in the same order that they are added. Uses the following operations

* `add(item)`: add item to end of list
* `remove()`: remove first item in the list
* `peek()`: return top of queue
* `isEmpty()`: true if and only if the queue is empty

A queue and a linked list are essentially the same thing as long as items are added and removed from opposite sides.

```java
public class MyQueue<T> {
    private static class QueueNode<T> {
        private T data;
        private QueueNode<T> next;

        public QueueNode(T data) {
            this.data = data;
        }
    }

    private QueueNode<T> first;
    private QueueNode<T> last;

    public void add(T item) {
        QueueNode<T> t = new QueueNode<T>(item);
        if (last != null){
            last.next = t;
        }
        last = t;
        if (first == null) {
            first = last;
        }
    }

    public T remove() {
        if(first == null) throw new NoSuchElementException();
        T data = first.data;
        first = first.next;
        if (first == null) {
            last = null;
        }
        return data;
    }

    public T peek() {
        if(first == null) throw new NoSuchElementException();
        return first.data;
    }

    public boolean isEmpty() {
        return first = null;
    }
}
```

It is very easy to mess up the updating of the first and the last nodes in a queue, remember to double check. Usually queues are used in breadth-first search or in implementing a cache.

In breadth-first search, a queue is used to store a list of the nodes that need to be processed. Each time a node is processed, we add its adjacent nodes to the back of the queue. this allows for nodes to be processed in the order they are viewed.
