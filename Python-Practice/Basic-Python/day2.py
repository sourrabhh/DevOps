import re
import day3 as cal

arn = "arn:aws:bkbdskfb:11 souraabh"
# print(arn.split("/"))
# print(arn.strip())

pattern = r"souraabh"

match = re.match(pattern, arn)

if match:
    print("Match  :: ", match.group())
else:
    print("Not Found")

cal.add()