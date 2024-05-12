import os
import time

COMMAND = 'Python -m unittest'
AUTH_COMMAND = COMMAND + ' tests.AuthTest'
FIND_COMMAND = COMMAND + ' tests.FindTest'
CART_COMMAND = COMMAND + ' tests.TestCart'
ORDER_COMMAND = COMMAND + ' tests.MakingOrderTest'

start_time = time.time()
os.system(AUTH_COMMAND)
os.system(FIND_COMMAND)
os.system(CART_COMMAND)
os.system(ORDER_COMMAND)
print(time.time() - start_time)