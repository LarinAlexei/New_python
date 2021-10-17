"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.

"""


class BinaryTree:
    def __init__(self, root_obj):  # корень
        self.root = root_obj  # левый потомок
        self.left_child = None  # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):  # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)  # если у узла есть левый потомок
        else:  # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)  # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):  # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)  # если у узла есть правый потомок
        else:  # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)  # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


""" Проверим результат: """

r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

""" Делаем ввод данных в древо, в ручном режиме: """

r = BinaryTree(8)

# Левая часть древа
r.insert_left(1)
r.insert_left(2)
r.insert_left(4)

# 1 - 3
root = r.left_child.left_child
print('2 <--> ', root.get_root_val())  # 2
root.insert_right(3)  # 3

# 4 - 6
root = r.left_child
print('4 <--> ', root.get_root_val())  # 4
root.insert_right(6)  # 6
root.right_child.insert_right(7)
root.right_child.insert_left(5)

# --- Пройдемся по правой части дерева
r.insert_right(15)
r.insert_right(14)
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

# 1 - 3
root = r.right_child.right_child
print('14 <--> ', root.get_root_val())  # 14
root.insert_left(13)  # 13

# 9 - 11
root = r.right_child
print('12 <--> ', root.get_root_val())  # 12
root.insert_left(10)  # 10
root.left_child.insert_right(11)
root.left_child.insert_left(9)

root = r.right_child.right_child.left_child
print('13 <--> ', root.get_root_val())  # 9
root = r.right_child.left_child.left_child
print('9 <--> ', root.get_root_val())  # 9