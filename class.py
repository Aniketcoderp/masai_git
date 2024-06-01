def root(n):
    if n==0 or n==1:
        return n
    l=0
    r=n
    ans=0
    while l<=r:
        mid=(l+r)//2
        if mid*mid==n:
            return mid
        if mid*mid<n:
            l=mid+1
            ans=mid
        else:
            r=mid-1
    return ans
n=4
print(root(n))
n=8
print(root(n))