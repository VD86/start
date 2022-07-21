from queue import Queue
from functools import partial

#петля событий
event_loop = None

class EventLoop(Queue):
  def start(self, limit=10):
    while True: #петля
      function = self.get() #взять из очереди
      function()
      limit -= 1
      if limit ==0: break

def buy_water():
  global event_loop
  print("Buying water")
  event_loop.put(buy_bread) #поставить в очередь

def buy_bread():
  global event_loop
  print("Buying bread")
  event_loop.put(buy_water) #поставить в очередь

event_loop = EventLoop()
event_loop.put(buy_water)
event_loop.start(limit=5)
