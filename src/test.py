
import logging
import os

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Get a logger instance (you can use __name__ for the current module's name)
logger = logging.getLogger(__name__)

def test():
    ENV_1 = os.getenv()
    logger.info("Test log message %s", ENV_1)