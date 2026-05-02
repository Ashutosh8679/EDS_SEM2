from datetime import date
from datetime import datetime

date1_str=input().strip()
date2_str=input().strip()

date1 = datetime.strptime(date1_str,"%Y-%m-%d")
date2 = datetime.strptime(date2_str,"%Y-%m-%d")

diff = date2-date1
print(diff.days)