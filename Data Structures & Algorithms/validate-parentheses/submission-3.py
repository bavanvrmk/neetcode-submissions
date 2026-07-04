class Solution:
    def isValid(self, s: str) -> bool:
        ll=[]
        for i in s:
            if i==')':
                if len(ll)==0:
                    return False
                if ll[-1]=='(':
                    ll.pop()
                else:
                    return False
            elif i==']':
                if len(ll)==0:
                    return False
                if ll[-1]=='[':
                    ll.pop()
                else:
                    return False
            elif i=='}':
                if len(ll)==0:
                    return False
                if ll[-1]=='{':
                    ll.pop()
                else:
                    return False
            else:
                ll.append(i)
        if len(ll)==0:
            return True
        return False