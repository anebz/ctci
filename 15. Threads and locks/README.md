# 15. Threads and locks

## Threads in Java

Every thread in Java is created and controlled by a unique object of the Java.lang.Thread class. When a standalone application is run, a user thread is automatically created to execute the `main()` method. This thread is called the main thread.

In Java, we can implement threads in two ways:

1. By implementing the java.lang.Runnable interface
2. By extending the java.lang.Thread class

### Implementing the runnable interface

```java
public interface Rnunable {
    void run();
}
```

1. Create a class which implements the Runnable interface. An object of this class is a Runnable object.
2. Create an object of type Thread by passing a Runnable object as argument to the Thread constructor. The Thread object now has a Runnable object that implements the run() method.
3. The start() method is invoked on the Thread object created in the previosu step.

```java
public class RunnableThreadExample implements Runnable {
    public int count = 0;

    public void run() {
        System.out.println("RunnableThread starting");
        try {
            while (count < 5) {
                Thread.sleep(500);
                count++;
            }
        } catch (InterruptedException exc) {
            System.out.println("RunnableThread interrupted");
        }
        System.out.println("RunnableThread terminating");
    }
}

public static void main(String[] args) {
    RunnableThreadExample instance = new RunnableThreadExample();
    Thread thread = new Thread(instance);
    thread.start();

    /* wait until above thread counts to 5 */
    while (instance.count != 5) {
        try {
            Thread.sleep(250);
        } catch {InterruptedException exc} {
            exc.printStackTrace();
        }
    }
}
```

### Extending the thread class

Or, we can override the run() method of the Thread class.

```java
public class ThreadExample extends Thread {
    int count = 0;

    public void run() {
        System.out.println("Thread starting");
        try {
            while (count < 5) {
                Thread.sleep(500);
                System.out.println("In Thread, count is " + count);
                count++;
            }
        } catch (InterruptedException exc) {
            System.out.println("Thread interrupted");
        }
        System.out.println("Thread terminating");
    }
}

public class ExampleB {
    public static void main(String args[]) {
        ThreadExample instance = new ThreadExample();
        instance.start();

        while (instance.count != 5) {
            try {
                Thread.sleep(250);
            } catch (InterruptedException exc) {
                exc.printStackTrace();
            }
        }
    }
}
```

## Synchronization and locks

Threads within a given process share ths ame memory space. It enables threads to share data, but it can create issues when the two threads modify a resource at the same time.

With the `synchronized` keyword, it can be applied to methods and code blocks, and it restricts multiple threads from executing the code simultaneously on the *same object*.

For more granular control, we can use a lock, which is used to synchronize access to a shared resource by associating the resource with the lock. A thread gets access to a shared resource by first acquiring the lock associated with the resource. At any given time, at most one thread can hold the lock and therefore, only one thread can access the shared resource.

## Deadlocks and deadlock prevention

In a deadlock situation, a thread is waiting for an object lock that another thread holds, and this second thread is waiting the an object lock that the first thread holds. In order for a deadlock to occur, all the following conditions must meet:

1. Mutual exclusion: only one process can access a resource at a given time
2. Hold and wait: processes already holding a resource can request additional resources, without relinquishing their current resources
3. No preemption: One process cannot forcibly remove another process' resource
4. Circular wait: 2+ processes from a circular chain where each process is waiting on another resource in the chain.

Deadlock prevention entails removing any of the above conditions.
