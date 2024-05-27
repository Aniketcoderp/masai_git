def sub(s,index,cur):
    if index==len(s):
        if cur:
            print(''.join(cur))
        return
    sub(s,index+1,cur+[s[index]])
    sub(s,index+1,cur)
n=4
s='abcd'
sub(s,0,[])
