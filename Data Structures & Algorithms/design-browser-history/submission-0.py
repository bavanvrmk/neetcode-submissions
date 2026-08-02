class Site:
    def __init__(self,url,prev=None,next=None):
        self.url=url
        self.next=next
        self.prev=prev
class BrowserHistory:
    def __init__(self, homepage):
        self.cur: Site = Site(homepage)  

    def visit(self, url: str) -> None:
        self.cur.next=Site(url,self.cur)
        self.cur.next.prev=self.cur
        self.cur=self.cur.next
        self.cur.next=None
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev:
            self.cur=self.cur.prev
            steps-=1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next:
            self.cur=self.cur.next
            steps-=1
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)