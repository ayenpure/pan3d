import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

__version__ = "0.13.1"

__all__ = [
    "logger",
    "__version__",
]
