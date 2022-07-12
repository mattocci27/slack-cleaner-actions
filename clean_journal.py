from slack_cleaner2 import SlackCleaner
import datetime
import sys

today = datetime.date.today()
day_delta = datetime.timedelta(days=-14)
day_target = today+day_delta
print(day_target)

day_str = day_target.strftime('%Y%m%d')
print(day_str)

s = SlackCleaner(sys.argv[1], sleep_for=1)

# list of users
s.users
# list of all kind of channels
s.conversations

# remove msg older than a month
for channel in ['journal-feed-general', 'journal-feed-plants']:
  print('deleting', s.c[channel], 'older than', day_target)
  for msg in s.c[channel].msgs(before=day_str, with_replies=True):
    msg.delete()
