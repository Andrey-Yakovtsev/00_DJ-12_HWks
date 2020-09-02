import requests
import datetime
from django import template
# from app.views import do_request

register = template.Library()


def do_request():
    resp = requests.get('https://reddit.com/r/Python/top.json',
                        headers={'User-Agent': 'Python Netology'})
    return resp.json()['data']['children']

@register.filter
def format_date(value):
    # Ваш код
    return value


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    # Ваш код
    return value



