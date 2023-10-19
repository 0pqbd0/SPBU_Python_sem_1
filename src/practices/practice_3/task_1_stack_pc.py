from dataclasses import dataclass
from collections import namedtuple
from typing import Any

StackElement = namedtuple("StackElement", ["next", "value"])


@dataclass
class Stack:
    size: int = 0
    head: StackElement = None


def empty(stack: Stack) -> bool:
    return stack.size == 0


def size(stack: Stack) -> int:
    return stack.size


def top(stack: Stack) -> Any:
    return stack.head.value


def push(stack: Stack, value) -> None:
    newelem = StackElement(next=stack.head, value=value)
    stack.head = newelem
    stack.size += 1


def pop(stack: Stack) -> any:
    if not empty(stack):
        popvalue = stack.head.value
        stack.head = stack.head.next
        stack.size -= 1
        return popvalue


if __name__ == "__main__":
    stack = Stack()
    iteration = int(input("Введите количество элементов стека:"))
    for i in range(iteration):
        elem = input("Введите элемент стека:")
        push(stack, elem)
    print("Ваш стек:")
    for i in range(iteration):
        print(pop(stack))