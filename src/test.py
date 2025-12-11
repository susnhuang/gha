
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
    logger.info("EXT_1 %s", ENV_1)
    value = os.getenv("DEFAULT_EXT_1", "") or os.getenv("EXT_1", "")
    logger.info("value %s", value)

    CNODE_USERNAME = os.getenv("CNODE_USERNAME", "")
    logger.info("CNODE_USERNAME %s", CNODE_USERNAME)

    CNODE_PASSWORD = os.getenv("CNODE_PASSWORD", "")
    logger.info("CNODE_PASSWORD %s", CNODE_PASSWORD)

    JNODE_USERNAME = os.getenv("JNODE_USERNAME", "")
    logger.info("JNODE_USERNAME %s", JNODE_USERNAME)

    JNODE_PASSWORD = os.getenv("JNODE_PASSWORD", "")
    logger.info("JNODE_PASSWORD %s", JNODE_PASSWORD)

if __name__ == "__main__":
    test()