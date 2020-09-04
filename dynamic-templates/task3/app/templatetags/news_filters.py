from django import template
import requests
import time
from datetime import timedelta, datetime
# from app.views import do_request

register = template.Library()


def do_request():
    resp = requests.get('https://reddit.com/r/Python/top.json',
                        headers={'User-Agent': 'Python Netology'})
    return resp.json()['data']['children']

@register.filter
def format_date(value2):
    posts = do_request()
    for post in posts:
        date = post['data']['created_utc']
        nowadays = datetime.now().timestamp()
        value2 = (nowadays - date)
        if value2//(60 * 60 * 24) > 24:
            value = f'Дата публикации {time.ctime(date)}'
        elif 600 < value2 < 60*60*24:
            hours = int(value2 // (60 * 60))
            value = f'{hours} часов назад'
        else:
            value = 'Только что'
    return value



@register.filter
def format_score(value):
    posts = do_request()
    for post in posts:
        value = post['data']['score']
        if value > 5:
            return 'Гениально'
        elif -1 < value < 5:
            return 'Neutral'
        else:
            return 'Total shit'



@register.filter
def format_num_comments(value):
    posts = do_request()
    for post in posts:
        # pprint(post)
        value = post['data']['num_comments']
        if value == 0:
            # print('Leave a comment')
            return 'Leave a comment'
        elif 0 < value < 50:
            # print(f'We have {comments} comments')
            return f'We have {value} comments'
        elif value > 50:
            # print('We have 50+ comments')
            return 'We have 50+ comments'


