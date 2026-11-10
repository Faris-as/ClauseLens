import logging
import sys
import redis
from rq import Connection, Queue, Worker

from app.core.config import get_settings
from app.core.logging import setup_logging

settings = get_settings()
setup_logging(debug=settings.DEBUG)
logger = logging.getLogger("clauselens.worker")


def start_worker() -> None:
    """Start listening on the ingestion job queue."""
    logger.info("Starting ClauseLens background worker...")
    redis_conn = redis.from_url(settings.REDIS_URL)

    with Connection(redis_conn):
        queue = Queue("clauselens_ingestion")
        worker = Worker([queue], connection=redis_conn)
        logger.info("Worker listening on queue: clauselens_ingestion")
        worker.work()


if __name__ == "__main__":
    try:
        start_worker()
    except KeyboardInterrupt:
        logger.info("Worker stopped by user.")
        sys.exit(0)
