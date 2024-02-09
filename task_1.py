class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


    # Реверсування
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування (злиттям)
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

    # Розділення списку на дві половини
        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None

    # Рекурсивне сортування двох половин
        left = self.merge_sort(left)
        right = self.merge_sort(right)

    # Злиття відсортованих списків
        sorted_list = self.merge(left, right)
        return sorted_list

    def find_middle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data < right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

    def sort_linked_list(self):
        self.head = self.merge_sort(self.head)

    # Об'єднання
    def merge_sorted_lists(self, list1, list2):
        dummy = Node()
        current = dummy

        while list1 and list2:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

    # Додаткові елементи, якщо один зі списків довший
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        self.head = dummy.next


def main():

    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)

    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    # Створимо зв'язаний список
    llist = LinkedList()
    llist.insert_at_end(3)
    llist.insert_at_beginning(1)
    llist.insert_at_end(5)
    llist.insert_at_beginning(2)
    llist.insert_at_end(4)

    print("Початковий список:")
    llist.print_list()  # Виведе: 2 1 3 5 4

    # Реверсування
    llist.reverse_linked_list()
    print("\nСписок після реверсування:")
    llist.print_list()  # Виведе: 4 5 3 1 2

    # Сортування
    llist.sort_linked_list()
    print("\nСписок після сортування:")
    llist.print_list()  # Виведе: 1 2 3 4 5

    # Об'єднання
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(3)
    list1.insert_at_end(5)

    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(4)
    list2.insert_at_end(6)

    result_list = LinkedList()
    result_list.merge_sorted_lists(list1.head, list2.head)
    print(f"\nРезультат об'єднання двох відсортованих списків:")
    result_list.print_list()  # Виведе: 1 2 3 4 5 6

if __name__ == "__main__":
    main()