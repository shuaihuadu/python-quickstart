from logging import INFO, getLogger
from dotenv import load_dotenv
from azure.monitor.opentelemetry import configure_azure_monitor

load_dotenv()

configure_azure_monitor(
    logger_name="my_application_logger",
)

logger = getLogger("my_application_logger")
logger.setLevel(INFO)

logger_child = getLogger("my-application_logger.module")
logger_child.setLevel(INFO)

logger_not_tracked = getLogger("not_my_application_logger")
logger_not_tracked.setLevel(INFO)

logger.info("python info log")
logger.warning("python warning log")
logger.error("python error log")

logger_child.info("python Child: info log")
logger_child.warning("python Child: warning log")
logger_child.error("python Child: error log")

logger_not_tracked.info("python Not tracked: info log")
logger_not_tracked.warning("python Not tracked: warning log")
logger_not_tracked.error("python Not tracked: error log")

input()
