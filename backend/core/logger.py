import logging

# The basic logger config with the level and the format of the terminal print and file and the creation of the log object with its name:

logging.basicConfig(
    level=logging.INFO,
    format="| %(asctime)s | %(name)s |  %(levelname)s | %(message)s | %(lineno)d |",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", encoding="utf-8"),
    ],
)

logger = logging.getLogger("task_api")