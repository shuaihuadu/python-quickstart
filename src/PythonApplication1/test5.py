from datetime import datetime, timezone, timedelta
import pytz

# 获取当前时间
current_time = datetime.now()

# 设置时区（例如，使用 UTC 时区）
timezone = pytz.timezone('UTC')

# 将当前时间转换为带时区的时间
current_time_with_timezone = current_time.astimezone(timezone)

# 格式化时间戳
formatted_timestamp = current_time_with_timezone.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_timestamp)


timestamp = datetime.now().isoformat()

print(timestamp)