from redis import Redis
from uuid import uuid4


class session:
    prefix = 'session_key:'
    host = os.environ['REDIS_URL']
    timeout = 3600

    def __init__(self):
        self.db = Redis(host)

    def create(self, user_name):
        session_key = str(uuid4())
        self.db.setex(self.prefix+session_key, user_name, self.timeout)

    def open(self, session_key):
        user_name = self.db.get(self.prefix+session_key)

        if user_name is not None:
            self.db.expire(self.prefix+session_key, self.timeout)
        return user_name