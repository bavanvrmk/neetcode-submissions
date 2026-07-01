class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        gr=arr[-1]
        i=len(arr)-2
        while i>-1:
            temp=arr[i]
            arr[i]=gr
            if temp>gr:
                gr=temp
            i-=1
        arr[-1]=-1
        return arr