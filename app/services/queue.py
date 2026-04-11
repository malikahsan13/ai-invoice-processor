import redis
import json

r = redis(host="localhost", port=6379, decode_responses=True)

QUEUE_NAME = "invoice_queue"


def push_job(data: dict):
    r.lpush(QUEUE_NAME, json.dumps(data))


def pop_job():
    job = r.rpop(QUEUE_NAME)
    return json.loads(job) if job else None
