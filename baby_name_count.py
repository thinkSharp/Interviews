import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node):
        if node is None:
            return
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def get_nodes(self):
        lst = set()
        ptr = self.head
        while ptr is not None:
            lst.add(ptr.data)
            ptr = ptr.next
        return lst

    def merge_list(self, ll):
        if ll is None:
            return

        ptr = ll.head
        while ptr is not None:
            self.add(Node(ptr.data))
            ptr = ptr.next


def baby_names_with_synonyms(names, synonyms):
    stack = collections.deque()
    new_values = []
    visited = set()
    new_synonyms = {}
    for s, sn in synonyms.items():
        val_1 = val_2 = None
        if s in new_synonyms:
            val_1 = new_synonyms[s]

        if sn in new_synonyms:
            val_2 = new_synonyms[sn]

        if val_1 is not None and val_2 is not None:
            val_1.merge_list(val_2)
            val_2.merge_list(val_1)
            val_1.add(Node(s))
            val_1.add(Node(sn))
            val_2.add(Node(s))
            val_2.add(Node(sn))
            val = val_1
        elif val_1 is not None:
            val = val_1
        elif val_2 is not None:
            val = val_2
        else:
            val = LinkedList()
        val.add(Node(s))
        val.add(Node(sn))

        if s in new_synonyms:
            new_synonyms[s] = val
        else:
            new_synonyms[s] = val
        if sn in new_synonyms:
            new_synonyms[sn] = val
        else:
            new_synonyms[sn] = val

    for k,v in names.items():
        stack.append((k,v, (set(), 0)))

    while stack:
        item = stack.popleft()
        k, v, result = item
        syn_set, total = result
        if k in visited:
            continue
        visited.add(k)
        syn_set = result[0]
        syn_set.add(k)
        total = total + v
        new_result = (syn_set, total)
        if k not in new_synonyms:
            new_values.append(new_result)
        else:
            edges_visited = True
            for sn in new_synonyms[k].get_nodes() - visited:
                edges_visited = False
                stack.appendleft((sn, names[sn], new_result))
            if edges_visited:
                new_values.append(new_result)
    print(new_synonyms)
    print(new_values)
    baby_names = {}
    for names,total in new_values:
        for name in names:
            if name in baby_names:
                if baby_names[name] < total:
                    baby_names[name] = total
            else:
                baby_names[name] = total
    return baby_names


def test_baby_names():
    names = {'john':10, 'jon':3, 'davis':2, 'kari':3, 'johnny':11, 'carlton':8, 'carleton':2, 'jonathan':9, 'carrie':5}
    synonyms = {'jonathan':'john', 'jon':'johnny', 'johnny':'john','kari':'carrie','carleton':'carlton'}
    result = baby_names_with_synonyms(names, synonyms)
    print(result)


test_baby_names()


