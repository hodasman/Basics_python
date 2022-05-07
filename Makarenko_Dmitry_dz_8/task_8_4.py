def val_checker(callback):
   def p_wrapper(func):
      def wrapper(args):
         result = func(args)
         if callback(args):
            print(result)
            return result
         else:
            raise ValueError(f'wrong val {args}')
            print(e)
      return wrapper
   return p_wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)