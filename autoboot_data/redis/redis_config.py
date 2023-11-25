from autoboot.annotation import component
from redis import Redis
from .redis_properties import RedisProperties

@component("redis_connection")
def connection() -> Redis:
  serve_mode = RedisProperties.serve_mode()
  if serve_mode == "single":
    return Redis(host=RedisProperties.host(),
        port=RedisProperties.port(),
        db=RedisProperties.db(),
        username=RedisProperties.username(),
        password=RedisProperties.password(),
        socket_timeout=RedisProperties.socket_timeout(),
        socket_connect_timeout=RedisProperties.socket_connect_timeout(),
        retry_on_timeout=RedisProperties.retry_on_timeout(),
        decode_responses=RedisProperties.decode_responses(),
        )
  
  elif serve_mode == "sentinel":
    from redis.sentinel import Sentinel
    
    sentinel_list = list(map(lambda n: tuple(n.split(":")[0], \
      int(n.split(":")[1])), RedisProperties.nodes()))
    sentinel = Sentinel(sentinel_list)
    master_client = sentinel.master_for(RedisProperties.sentinel_service_name(),\
      decode_responses=RedisProperties.decode_responses())
    slave_client = sentinel.slave_for(RedisProperties.sentinel_service_name(), \
      decode_responses=RedisProperties.decode_responses())
    return master_client or slave_client
  
  elif serve_mode == "cluster":
    from redis import RedisCluster
    from redis.cluster import ClusterNode
    
    cluster_nodes = list(map(lambda n: ClusterNode(host=n.split(":")[0], \
      port=int(n.split(":")[1])), RedisProperties.nodes()))
    cluster = RedisCluster(startup_nodes=cluster_nodes, \
      decode_responses=RedisProperties.decode_responses())
    return cluster
