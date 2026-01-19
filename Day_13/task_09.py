import time

class Timer:
  def __enter__(self):
    self.t = time.time()
    time.sleep(2)

  def __exit__(self, *args):
    print(time.time() - self.t)

with Timer():
    time.time() 
