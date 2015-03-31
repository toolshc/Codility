# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, Y, D):
    # write your code in Python 2.7
    distance = Y-X
    if distance % D == 0 :
      return distance/D
    else :
      return distance/D + 1

print solution(0,5,2)
print solution(10,85,30)