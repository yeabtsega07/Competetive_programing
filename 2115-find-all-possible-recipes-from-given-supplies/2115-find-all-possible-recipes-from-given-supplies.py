class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        check = set(supplies)
        graph = defaultdict(list)
        inDegree = defaultdict(set)
        
        for index , recipe in enumerate(recipes):
            
            for ingredient in ingredients[index]:
                
                if ingredient not in check:
                    graph[ingredient].append(recipe)
                    inDegree[recipe].add(ingredient)
        
        queue = deque()
        for recipe in recipes:
            if recipe not in inDegree:
                queue.append(recipe)
        
        visited = set()
        result = []
        while queue:
            
            cur = queue.popleft()
            result.append(cur)
            
            for child in graph[cur]:
                inDegree[child].remove(cur)
                
                if not inDegree[child]:
                    queue.append(child)
                    visited.add(child)
        
        return result