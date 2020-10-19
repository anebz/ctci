# 13. Java

## Overloading vs. overriding

* Overloading: two methods have the same name, but differ in the type or number of alignments.
* Overriding: a method shares the same name and function signature as another method in its super class

## Collection framework

* ArrayList: dynamically resizing array, growing as you insert elements
* Vector: similar to ArrayList, but synchronized
* LinkedList
* HashMap

```java
ArrayList<String> myArr = new ArrayList<String>();
myArr.add("one");
myArr.add("two");
System.out.println(myArr.get(0));

Vector<String> myVec = new Vector<String>();
myVec.add("one");
myVec.add("two");
System.out.println(myVec.get(0));

LinkedList<String> myLinkedList = new LinkedList<String>();
myLinkedList.add("two");
myLinkedList.addFirst("one");
Iterator<String> iter = myLinkedList.iterator();
while (iter.hasNext()) {
    System.out.println(iter.next());
}

HashMap<String, String> map = new HashMap<String, String>();
map.put("one", "uno");
map.put("two", "dos");
System.out.println(map.get("one"));
```
