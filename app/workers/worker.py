import time
from app.services.queue import pop_job


def process_job(job):
    print(f"Prossing {job}")


def start_worker():
    print("Worker started...")

    while True:
        job = pop_job()

        if job:
            try:
                process_job(job)
            except Exception as e:
                print("Error:", e)
        else:
            time.sleep(2)
