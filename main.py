import schedule
import time
from email import delete_email, empty_trash

# 하루에 한 번 오후 10시에 오늘 이메일이 아닌 메일 삭제
schedule.every().day.at('22:00').do(delete_email)

# 매주 일요일 오전 10시에 메일 휴지통의 모든 메일 삭제
schedule.every().sunday.at('10:00').do(empty_trash)

while True:
    schedule.run_pending()
    time.sleep(1)
