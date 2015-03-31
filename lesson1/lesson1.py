#time complexity

def constant(n):
  result = n * n
  return result

#print constant(6)

def logarithmic(n):
  result = 0
  while n > 1:
    n //= 2
    result += 1
  return result

#print logarithmic(16)
#print logarithmic(32)

def linear(n, A):
  for i in xrange(n):
    if A[i] == 0:
      return 0
  return 1

A = [1,2,3,4,5]
#print linear(5, A)

def quadratic(n):
  result = 0
  for i in xrange(n):
    for j in xrange(i, n):
      result += 1
  return result

print quadratic(5)

def linear2(n, m):
  result = 0
  for i in xrange(n):
    result += i
  for j in xrange(m):
    result += j
  return result

print linear2(3,2)

#space complexity
