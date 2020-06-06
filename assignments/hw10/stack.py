"""
class Stack:
"""

if __name__ == '__main__':
    s = Stack()
    print(s.empty()) # True
    s.push(1)
    print(s.empty()) # False
    s.push(2)
    s.push(3)
    print(s.peek()) # 3
    print(s.pop()) # 3
    print(s.peek()) # 2
    print(s)
