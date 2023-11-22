from autoboot import AutoBoot, AutoBootConfig
from autoboot_data import redis

def setup_module():
  autoboot = AutoBoot(config=AutoBootConfig(config_dir="./tests/test_redis"))
  autoboot.run()
  
def test_redis():
  r = redis.connection()
  assert r.ping()