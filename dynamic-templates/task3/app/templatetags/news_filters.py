from django import template
import time
from datetime import timedelta, datetime


register = template.Library()


@register.filter
def format_date(value):
    nowadays = int(datetime.now().timestamp())
    value2 = (nowadays - value)
    if value2//(60 * 60 * 24) > 24:
        return f'Дата публикации {time.ctime(value)}'
    elif 600 < value2 < 60*60*24:
        hours = int(value2 // (60 * 60))
        return f'{hours} часов назад'
    else:
        return 'Только что'



@register.filter
def format_score(value):
    if value > 5:
        return 'Гениально'
    elif -1 < value < 5:
        return 'Neutral'
    else:
        return 'Total shit'



@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Leave a comment'
    elif 0 < value < 50:
        return f'We have {value} comments'
    elif value > 50:
        return 'We have 50+ comments'


