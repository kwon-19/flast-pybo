def format_datetime(value, fmt : str = '%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)