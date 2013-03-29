# Cache decorator
def cache(fn):
  cache = {}
  
  def wrapper(*args):
    if args in cache:
      return cache[args]
    else:
      rv = fn(*args)
      cache[args] = rv
      return rv
  return wrapper


def next_num(num):
  if num % 2 == 0:
    return num / 2
  else:
    return 3 * num + 1
    
    
# This function is cached
# I actually tried caching the other one, but it slowed the program down!    
@cache
def seq_len(num):
  if num == 1:
    return 1
  else:
    # Here using recursion to use the cache
    return seq_len(next_num(num)) + 1
    
# And I like this functional bit here at the end
print max([(x, seq_len(x)) for x in xrange(1, 1000000)], key=lambda x: x[1])[0]





