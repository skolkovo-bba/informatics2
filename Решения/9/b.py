# Решение задачи "Двоичное дерево поиска"

# функция, проверяющая является ли поддерево корректным двоичным деревом поиска
def is_binary_tree(tree, root, min_value, max_value):
    # если корень равен -1, значит, дерево пустое, следовательно, оно корректно
    if root == -1:
        return True
    # если значение в корне не находится в указанных пределах, то дерево не является двоичным поисковым
    if not min_value < tree[root][0] < max_value:
        return False
    # проверяем левое поддерево
    left_valid = is_binary_tree(tree, tree[root][1], min_value, tree[root][0])
    # проверяем правое поддерево
    right_valid = is_binary_tree(tree, tree[root][2], tree[root][0], max_value)
    # возвращаем результат
    return left_valid and right_valid

# считываем количество вершин
n = int(input())

# считываем описание вершин и сохраняем в словарь
tree = {}
for i in range(n):
    value, left, right = map(int, input().split())
    tree[i] = (value, left, right)

# проверяем корректность дерева
result = is_binary_tree(tree, 0, float('-inf'), float('inf'))

# выводим результат
if result:
    print("YES")
else:
    print("NO")