class A:
    def hello(self):
        print("A")

class C(A):
    def hello(self):
        print("C")
        super().hello()
```

Kodni ishlatish uchun misol:
```python
c = C()
c.hello()  # Chiqaradi: C, A
