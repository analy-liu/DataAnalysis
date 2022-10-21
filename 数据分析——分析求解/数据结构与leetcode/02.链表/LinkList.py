# 链表实现
class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    """单列表"""

    def __init__(self, node = None):
        self._head = node
        
    def is_empty(self):
        """判断列表是否为空"""
        return self._head == None

    def travel(self):
        """遍历整个列表"""
        cur = self._head
        array = []
        while cur != None:
            array.append(cur.elem)
            cur = cur.next
        print(array)

    def append(self, itemList):
        """链表尾部添加节点"""
        for item in itemList:
            node = Node(item)
            if self.is_empty():
                self._head = node
            else:
                cur = self._head
                while cur.next != None:
                    cur = cur.next
                cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 判断此节点是否是头节点
                # 头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

def Inverse_add(l1, l2):
    # 两个链表逆序相加
    sumList = Node(0)
    cur1, cur2, p= l1._head, l2._head, sumList
    temp = 0
    while cur1 or cur2 or temp != 0:
        n = (cur1.elem if cur1 else 0)+(cur2.elem if cur2 else 0)+temp
        temp = n//10
        p.next = Node(n % 10)
        p = p.next
        cur1 = cur1.next if cur1 else None
        cur2 = cur2.next if cur2 else None
    return sumList.next