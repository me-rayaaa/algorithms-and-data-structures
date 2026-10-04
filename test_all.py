from structures import MyArray, LinkedList, Deque, AVLTree
from sortings import bubble_sort, quick_sort

def test_array():
    a = MyArray()
    a.append(1)
    a.append(2)
    assert a.get(0) == 1
    assert len(a) == 2

def test_linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]

def test_deque():
    dq = Deque()
    dq.push_back(1)
    dq.push_front(0)
    assert dq.pop_front() == 0
    assert dq.pop_back() == 1

def test_avl():
    tree = AVLTree()
    root = None
    for i in [10, 20, 30, 40, 50]:
        root = tree.insert(root, i)
    assert root.key == 20
    assert root.left.key == 10
    assert root.right.key == 40

def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]

def test_quick_sort():
    assert quick_sort([3, 1, 2]) == [1, 2, 3]
    assert quick_sort([5, 5, 1]) == [1, 5, 5]