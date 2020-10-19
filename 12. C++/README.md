# 12. C++

## Classes and inheritance

```cpp
#include <iostream>
using namespace std;

// Base class
class Shape {
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
   protected:
      int width;
      int height;
};

// Derived class
class Rectangle: public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};

int main(void) {
   Rectangle Rect;
   Rect.setWidth(5);
   Rect.setHeight(7);

   // Print the area of the object.
   cout << "Total area: " << Rect.getArea() << endl;
   return 0;
}
```

## Constructors and destructors

```cpp
// constructor
Person(int w, h) {
    height = h;
    width = w;
}

// destructor
~Person() {
    delete height;
    delete width;
}
```

## Virtual functions

Setting a parent class function in the children class, inheritance.

## Pointers and reference

```cpp
// pointers
int* p = new int;
*p = 7;
int* q = p;
*q = 8
cout << *q; // prints 8

// references
int a = 5;
int& b = a;
b = 7;
cout << a; // prints 7

// pointer arithmetic
int* p = new int[2];
p[0] = 0;
p[1] = 1;
p++;
cout << *p; // prints 1
```
