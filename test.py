from datetime import datetime

today = datetime.now()

date = today.strftime('%Y-%m-%d %H:%M:%S')
print(date)