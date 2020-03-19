from redis import Redis


redis = Redis(os.environ['REDIS_URL'])