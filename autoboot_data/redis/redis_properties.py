from autoboot.annotation import value_component

class RedisProperties:
  
  @value_component("autoboot.data.redis.host")
  @staticmethod
  def host() -> str:
    return "127.0.0.1"
  
  @value_component("autoboot.data.redis.port")
  @staticmethod
  def port() -> int:
    return 6379
  
  @value_component("autoboot.data.redis.db")
  @staticmethod
  def db() -> int:
    return 0
  
  @value_component("autoboot.data.redis.username")
  @staticmethod
  def username() -> str:
    return None
  
  @value_component("autoboot.data.redis.password")
  @staticmethod
  def password () -> str:
    return None
  
  @value_component("autoboot.data.redis.socket_timeout")
  @staticmethod
  def socket_timeout() -> int:
    return 60
  
  @value_component("autoboot.data.redis.socket_connect_timeout")
  @staticmethod
  def socket_connect_timeout() -> int:
    return 30
  
  @value_component("autoboot.data.redis.retry_on_timeout")
  @staticmethod
  def retry_on_timeout() -> bool:
    return False
  
  @value_component("autoboot.data.redis.decode_responses")
  @staticmethod
  def decode_responses() -> bool:
    return True
  
  @value_component("autoboot.data.redis.serve_mode")
  @staticmethod
  def serve_mode() -> str:
    """ Serve mode value must be single, sentinel or cluster. """
    return "single"
  
  @value_component("autoboot.data.redis.nodes")
  @staticmethod
  def nodes() -> list[str]:
    return []
  
  @value_component("autoboot.data.redis.sentinel_service_name")
  @staticmethod
  def sentinel_service_name() -> str:
    return "master"

  
  