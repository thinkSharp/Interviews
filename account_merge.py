import collections
class DSU:
    def __init__(self):
        self.p = [i for i in range(10001)]

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


def accountsMerge(accounts):
    dsu = DSU()
    em_to_name = {}
    em_to_id = {}
    i = 0
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            em_to_name[email] = name
            if email not in em_to_id:
                em_to_id[email] = i
                i += 1
            dsu.union(em_to_id[acc[1]], em_to_id[email])

    ans = collections.defaultdict(list)
    for email in em_to_name:
        ans[dsu.find(em_to_id[email])].append(email)

    return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]

def accountsMerge1(accounts):
    graph = collections.defaultdict(set)
    em_to_name = {}
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            graph[account[1]].add(email)
            graph[email].add(account[1])
            em_to_name[email] = name

    seen = set()
    answer = []
    stack = collections.deque()
    for email in graph:
        if email in seen:
            continue

        seen.add(email)
        stack.append(email)
        component = []
        while stack:
            item = stack.pop()
            component.append(item)
            for new_email in graph[item]:
                if new_email not in seen:
                    seen.add(new_email)
                    stack.append(new_email)
        answer.append([em_to_name[email]] + sorted(component))

    return answer

def test_accountsMerge():
    result = accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"],["John", "john00@mail.com", "john01@mail.com", "john02@mail.com"]])
    print(result)

test_accountsMerge()

d = DSU()

v = d.find(10)
print(v)

d.union(10,15)
v = d.find(15)
print(v)




