import logging
from logging_config import setup_logging

#logging.basicConfig(
#    level = logging.INFO,
#    format = "%(asctime)s - %(levelname)s - %(message)s"
#)

#logging.debug("调试信息")
#logging.info("程序已启动")
#logging.warning("磁盘空间不足")
#logging.error("读取文件失败")
#logging.critical("服务不可用")

setup_logging(logging.INFO)

logger = logging.getLogger(__name__)

logger.info("服务启动")

try:
    logger.info("任务执行成功")
except Exception:
    logger.exception("任务执行失败")

def main():

    print("")



if __name__ == "__main__":
    main()