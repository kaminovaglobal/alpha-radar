import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "%(levelname)s "
        "%(message)s"
    )
)

logger = logging.getLogger(
    "alpharadar"
)

try:

    collect_jobs()

except Exception as e:

    logger.error(
        f"Collector failed: {e}"
    )

logger.error(
    {
      "collector":"jobs",
      "error":"timeout"
    }
)    