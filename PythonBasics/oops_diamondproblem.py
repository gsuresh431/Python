'''
    A
    /\
   B  C
    \/
    D 

    - This is an issue which is caused due to multiple inheritance
    - Multiple inheritance causes many such issues 
    - So, multiple inheritance is not supported in many languages
    - Instead we should use multilevel inheritance if required

    diamond problem:
    - now suppose A,B,C has a method demo()
    - Q. so, which demo() does D object gets ? 
    - Python handles this by using the order
    - class D(B, C) 
        - D will get demo() of B
    - class D(C, b)
        - D will get demo() of C
    - so, no issues for python
    - but this causes issues in other languages where the ordering has no role
      and the compiler gets confused as to which demo() should D get.

'''
class A:
    def demo(self):
        print("Demo of class A")

class B(A):
    def demo(self):
        print("Demo of class B")

class C(A):
    def demo(self):
        print("Demo of class C")

class D(B, C):
    pass

d = D()
print(dir(d))
print(d.demo())