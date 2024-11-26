from datetime import datetime, timezone, timedelta
import pytz

# ��ȡ��ǰʱ��
current_time = datetime.now()

# ����ʱ�������磬ʹ�� UTC ʱ����
timezone = pytz.timezone('UTC')

# ����ǰʱ��ת��Ϊ��ʱ����ʱ��
current_time_with_timezone = current_time.astimezone(timezone)

# ��ʽ��ʱ���
formatted_timestamp = current_time_with_timezone.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_timestamp)


timestamp = datetime.now().isoformat()

print(timestamp)