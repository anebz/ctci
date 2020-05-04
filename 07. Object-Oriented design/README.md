# Chapter 7 Object oriented design

OOP questions are about demonstrating that you understand how to create elegant, maintainable object-oriented code.

1. Handle ambiguity: many questions are intentionally vague, so that you ask questions. Who's going to use it, how.
2. Define the core objects: if it's a restaurant, the core objects might be table, guest, party, etc.
3. Analyze relationships between the objects. Which objects are member of other objects, which inherit from which, are relationships many-to-many or one-to-many? Party should have an array of guests, server and host inherit from employee, etc.
4. Investigate actions: what will objects do

## Design patterns

### Singleton class

This pattern ensures that a class has only one instance and ensures access to the instant through the application, it can be useful where you have a global object with exactly one instance. We might want to implement `Restaurant` with exactly one instance of Restaurant. Many people dislike this pattern, because it can interfere with unit testing.

```java
public class Restaurant {
    private static Restaurant _instance = null;
    protected Restaurant() {...}
    public static Restaurant getInstance() {
        if (_instance == null) {
            _instance = new Restaurant();
        }
        return _instance;
    }
}
```

### Factory method

It offers an interface for creating an instance of a class, with its subclasses deciding which class to instantiate.

```java
public class CardGame {
    public static CardGame createCardGame (GameType type) {
        if (type == Gametype.Poker) {
            return new PokerGame();
        } else if (type == Gametype.BlackJack) {
            return new BlackJackGame();
        }
        return null;
    }
}
```

## Resouces

* [C++ solutions](https://github.com/careercup/CtCI-6th-Edition/tree/master/Java/Ch%2007.%20Object-Oriented%20Design)