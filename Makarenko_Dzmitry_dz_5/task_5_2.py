n = 21
nums_gen = (num for num in range(1, n + 1, 2))

for _ in range(1, n + 1, 2):
    print(next(nums_gen))
# next(nums_gen)  # если раскомментировать, то должно падать в traceback по StopIteration