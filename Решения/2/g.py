tree = {
    'C': {'A', 'B'},
    'F': {'C'},
    'D': {'C'},
}

def parents(tree, name):
    return tree.get(name, set())

def grandparents(tree, name):
    ans = set()
    for par in tree.get(name, set()):
        ans |= tree.get(par, set())
    return ans

def children(tree, name):
    ans = set()
    for key in tree:
        if name in tree.get(key, set()):
            ans.add(key)
    return ans

def grandchildren(tree, name):
    ans = set()
    for chi in children(tree, name):
        ans |= children(tree, chi)
    return ans

def siblings(tree, name):
    ans = set()
    for key in tree:
        if tree.get(key, set()) == parents(tree, name):
            ans.add(key)
    return ans - {name}

print(parents(tree, 'C'))
print(parents(tree, 'A'),
    grandparents(tree, 'D'),

    grandparents(tree, 'C'),

    children(tree, 'A'),

    children(tree, 'D'),

    grandchildren(tree, 'A'),

grandchildren(tree, 'F'),

siblings(tree, 'F'),

siblings(tree, 'C'), sep="\n"
)

"""parents(tree, 'C')
    {'B', 'A'}
    parents(tree, 'A')
    set()
    grandparents(tree, 'D')
    {'B', 'A'}
    grandparents(tree, 'C')
    set()
    children(tree, 'A')
    {'C'}
    children(tree, 'D')
    set()
    grandchildren(tree, 'A')
    {'F', 'D'}
grandchildren(tree, 'F')
set()
siblings(tree, 'F')
{'D'}
siblings(tree, 'C')
set()"""