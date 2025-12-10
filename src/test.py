
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
    logger.info("Running test function")
    ENV_1 = os.getenv("EXT_1", "")
    logger.info("Test log message %s", ENV_1)
    if ENV_1 == "default_value":
        logger.info("default")
   
if __name__ == "__main__":
    test()