import random

print('Hello World!!! Welcome to python world!!!')
print('Good luck with you~~')

lotto = [n for n in range(1, 46)]

print('Go buy lotto now')

for i in range(5):
  print(random.sample(lotto, 6))
