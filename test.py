

print(2, end=',')
for i in range(3, 100, 2):
  for j in range(3, int(i ** .5) + 1, 2):
   if i % j == 0:
    break
   else:
    print(i, end=',')