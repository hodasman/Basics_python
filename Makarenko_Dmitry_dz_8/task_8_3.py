def type_logger(func):
   def wrapper (*args, **kwargs):
      list = []
      for arg in args:
         list.append(f'{func.__name__}({arg}: {type(arg)}) = {func(arg)}: {type(func(arg))}')
      for val in kwargs.values():
         list.append(f'{func.__name__}({val}: {type(val)}) = {func(val)}: {type(func(val))}')
      print(', '.join(list))
   return wrapper




@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5, 7, 10)