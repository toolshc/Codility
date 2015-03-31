def fast_solution(n):
  result = 0
  for i in xrange(n):
    result += (i + 1)
  return result

print fast_solution(4)
