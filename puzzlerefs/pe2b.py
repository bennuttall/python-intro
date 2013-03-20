def fib():
  a, b = 0, 1
  while 1:
    yield b
    a, b = b, a+b

f = fib()
sum = 0
while True:
  term = f.next()
  if term > 4000000: break
  if term % 2 == 0: sum += term
print sum