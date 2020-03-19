import os
from redis import Redis
from uuid import uuid4


class RedisSession:
    prefix = 'session_key:'
    host = os.environ['REDIS_HOST']
    port = os.environ['REDIS_PORT']
    timeout = 3600

    def __init__(self):
        self.db = Redis(self.host, self.port)

    def create_session(self, user_name):
        session_key = str(uuid4())
        self.db.setex(self.prefix+session_key, self.timeout, user_name)
        return session_key

    def open_session(self, session_key):
        user_name = self.db.get(self.prefix+session_key)

        if user_name is not None:
            self.db.expire(self.prefix+session_key, self.timeout)
        return user_name