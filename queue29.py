from collections import deque

queue= deque(['rohim','korim','joshim','salam','kalam'])# in queue first to enter first to out
print(queue)
queue.popleft() #if we use only pop it will dlt from last nd if we use popleft it will dlt from first
print(queue)
queue.appendleft('jorina') #if we use only append it will add from last nd if we use appendleft it will add from first
print(queue)