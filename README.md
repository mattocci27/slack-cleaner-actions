# Github actions for slack_cleaner2

Github Actions automatically deletes messages in `journal-feed-general` and `journal-feed-plants` older than 14 days everyday.

Or manually run:

```
# pip install slack-cleaner2
python3 clean_journal.py ${{ secrets.SLACK_LEGACY_TOKEN }}
```

Credits:
- slack_cleaner2: Samuel Gratzl (https://github.com/sgratzl/slack_cleaner2)
