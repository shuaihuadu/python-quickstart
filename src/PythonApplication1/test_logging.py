import logging  
  
# 创建一个日志记录器  
logger = logging.getLogger('my_logger')  
logger.setLevel(logging.DEBUG)  
  
# 检查是否已经有处理器，避免重复添加  
if not logger.hasHandlers():  
    # 创建一个控制台处理器  
    console_handler = logging.StreamHandler()  
    console_handler.setLevel(logging.DEBUG)  
  
    # 创建一个格式化器并设置时间格式  
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
  
    # 将格式化器添加到处理器  
    console_handler.setFormatter(formatter)  
  
    # 将处理器添加到日志记录器  
    logger.addHandler(console_handler)  
  
# 记录一条日志  
logger.debug('This is a debug message')  