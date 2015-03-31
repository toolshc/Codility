# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    lower_value = min(A)
    size = len(A)
    centinel = lower_value
    for i in xrange(size):
      if ( centinel not in A ) :
        return centinel
      else :
        centinel = centinel + 1

A = [2,3,1,5]

print solution(A);
