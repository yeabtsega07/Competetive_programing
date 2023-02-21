class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.currentPage = 0
        

    def visit(self, url: str) -> None:
        
        while len(self.stack) - 1 > self.currentPage:
            self.stack.pop()
            
        self.stack.append(url)
        self.currentPage += 1
        

    def back(self, steps: int) -> str:
        
        if steps <= self.currentPage:
            self.currentPage -= steps
            
        
        else:
            self.currentPage = 0
        
        return self.stack[self.currentPage]

    def forward(self, steps: int) -> str:
        
        if len(self.stack) > self.currentPage + steps:
            self.currentPage += steps
        else:
            self.currentPage = len(self.stack) - 1
            
        return self.stack[self.currentPage]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)