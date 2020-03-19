import os
from redis import Redis
from uuid import uuid4


class RedisSession:
    prefix = 'session_key:'
    host = os.environ['REDIS_HOST']
    port = os.environ['REDIS_PORT']
    timeout = 3600

    def __init__(self):
        self.db = Redis(self.host, self.port, charset="utf-8", decode_responses=True)

    def create_session(self, user_id):
        session_key = str(uuid4())
        self.db.setex(self.prefix+session_key, self.timeout, user_id)
        return session_key

    def open_session(self, session_key):
        user_id = self.db.get(self.prefix+session_key)

        if user_id is not None:
            self.db.expire(self.prefix+session_key, self.timeout)
        return user_id
    
    def delete_session(self, session_key):
        self.db.delete(self.prefix+session_key)