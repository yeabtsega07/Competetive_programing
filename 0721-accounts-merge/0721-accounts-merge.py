class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        class UnionFind:
            def __init__(self, emails):
                self.root = { i:i for i in emails  }
                self.rank = { i: 0 for i in emails }

            def find(self, member):

                root = member
                while root != self.root[root]:
                    root = self.root[root]

                while member != root:
                    parent = self.root[member]
                    self.root[member] = root
                    member = parent

                return root

            def union(self, x, y):

                rootX = self.find(x)
                rootY = self.find(y)

                if rootX != rootY:

                    if self.rank[rootX] > self.rank[rootY]:

                        self.root[rootY] = rootX

                    elif self.rank[rootX] < self.rank[rootY]:

                        self.root[rootX] = rootY

                    else:

                        self.root[rootY] = rootX
                        self.rank[rootX] += 1


            def connected(self, x, y):
                return self.find[x] == self.find[y]

        emails = set()
        track = defaultdict(list)
        for ac in accounts:
            owner = ac[0]
            for val  in ac[1:]:
                track[val].append(owner)
                emails.add(val)

        graph = UnionFind(emails)
        for ac in accounts:
            owner = ac[0]
            email = ac[1]
            for val  in ac[2:]:
                graph.union(email, val)

        check = defaultdict(list)
        for val in emails:
            cur = graph.find(val)
            check[cur].append(val)
        
        res = []
        for key in check:
            res.append([track[key][0]] + sorted(check[key]))
        
        return res
        