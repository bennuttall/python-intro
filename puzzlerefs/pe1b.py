print reduce(
  lambda x, y: x+y,
  filter(lambda x: 
    x%3==0 or x%5==0,
    xrange(1, 1000)
  )
)