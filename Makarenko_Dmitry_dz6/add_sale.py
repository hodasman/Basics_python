import sys
import os
cost = sys.argv[1]
with open(os.path.join(os.getcwd(), 'bakery.csv'), 'a') as f:
    f.write(cost)
    f.write('\r\n')

