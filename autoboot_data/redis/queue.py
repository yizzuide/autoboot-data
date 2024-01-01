import pickle
import uuid
from redis import Redis

class SimpleTask(object):
  def __init__(self, func, *args):
    self.func = func
    self.args = args
    self.id = str(uuid.uuid4())

  def process_task(self):
    self.func(*self.args)

class SimpleQueue(object):
  def __init__(self, conn: Redis, name):
    self.conn = conn
    self.name = name
  
  def push(self, func, *args):
    task = SimpleTask(func, *args)
    serialized_task = pickle.dumps(task, protocol=pickle.HIGHEST_PROTOCOL)
    self.conn.lpush(self.name, serialized_task)
    return task.id
  
  def pop(self) -> SimpleTask:
    _, serialized_task = self.conn.brpop(self.name)
    task = pickle.loads(serialized_task)
    task.process_task()
    return task
  
  def length(self):
    return self.conn.llen(self.name)
  