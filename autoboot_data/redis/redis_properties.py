from autoboot.annotation import static_property

class RedisProperties:
  
  @static_property("autoboot.data.redis.host")
  def host() -> str:
    return "127.0.0.1"
  
  @static_property("autoboot.data.redis.port")
  def port() -> int:
    return 6379
  
  @static_property("autoboot.data.redis.db")
  def db() -> int:
    return 0
  
  @static_property("autoboot.data.redis.username")
  def username() -> str:
    return None
  
  @static_property("autoboot.data.redis.password")
  def password () -> str:
    return None
  
  @static_property("autoboot.data.redis.socket_timeout")
  def socket_timeout() -> int:
    return 60
  
  @static_property("autoboot.data.redis.socket_connect_timeout")
  def socket_connect_timeout() -> int:
    return 30
  
  @static_property("autoboot.data.redis.retry_on_timeout")
  def retry_on_timeout() -> bool:
    return False
  
  @static_property("autoboot.data.redis.decode_responses")
  def decode_responses() -> bool:
    return True
  
  @static_property("autoboot.data.redis.serve_mode")
  def serve_mode() -> str:
    """ Serve mode value must be single, sentinel or cluster. """
    return "single"
  
  @static_property("autoboot.data.redis.nodes")
  def nodes() -> list[str]:
    return []
  
  @static_property("autoboot.data.redis.sentinel_service_name")
  def sentinel_service_name() -> str:
    return "master"

  
  