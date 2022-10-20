class Solution:
    def majorityElement(self, A, N):
        #Your code here
        m={}
        for i in A:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        c=0
        for i in m:
            if m[i]>N/2:
                c=1
                return i
        if c==0:
            return -1
