def slow_solution(n):
  result = 0
  for i in xrange(n):
    for j in xrange(i + 1):
      result += 1
  return result

print slow_solution(4)
