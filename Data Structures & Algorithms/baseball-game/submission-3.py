class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        idx=-1
        for i in range(len(operations)):
            print(i,idx,score)
            if operations[i]=="+":
                score.append(score[idx]+score[idx-1])
                idx+=1
            elif operations[i]=="D":
                score.append(2*score[idx])
                idx+=1
            elif operations[i]=="C":
                score.pop()
                idx-=1
            else:
                score.append(int(operations[i]))
                idx+=1
        return sum(score)
