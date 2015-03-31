def solution(A):
    should_be = len(A) # you never see N+1 in the iteration
    sum_is = 0
 
    for idx in xrange(len(A)):
        sum_is += A[idx]
        should_be += idx+1
 
    return should_be - sum_is +1

A = [2,3,1,5]

print solution(A);
