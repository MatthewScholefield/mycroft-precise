import redis
redis_host = "localhost"
redis_port = 6379
redis_password = "hakan"

class _PubSub(redis.client.PubSub):
    def run_in_thread(self):
        super(_PubSub, self).run_in_thread(sleep_time=0.001, daemon=True)

class StrictRedis(redis.StrictRedis):
    def pubsub(self, **kwargs):
        return _PubSub(self.connection_pool, **kwargs)

class RedisClient():
    r = StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)    
    
    @classmethod
    def pubsub_instance(cls):
        pubsub = cls.r.pubsub()
        return pubsub

    @classmethod
    def publish(cls,channel,msg):
        cls.r.publish(channel,msg)
