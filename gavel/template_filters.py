from gavel import app
from humanize import naturaltime

@app.template_filter('utcdatetime_local')
def _jinja2_filter_datetime_local(datetime):
    if datetime is None:
        return 'None'
    return naturaltime(datetime)

@app.template_filter('utcdatetime_epoch')
def _jinja2_filter_datetime_epoch(datetime):
    if datetime is None:
        return 0
    datetime_res = 0
    try:
        datetime_res = datetime.strftime('%s')
    except Exception as e:
        pass
    return datetime_res
