import requests
import json
import csv
from datetime import date, timedelta, datetime
from multiprocessing.dummy import Pool

def _on_success(r):
    print('Request crawl succeed')

def _on_error(ex):
    print('Requests crawl failed')

def _on_success_convert(r):
    print('Request convert succeed')

def _on_error_convert(ex):
    print('Requests convert failed')


def _call_requests_parallel(start_date, end_date, app_id):
    pool = Pool(10)
    day_count = (end_date - start_date).days + 1
    response_result = []
    for single_date in (start_date + timedelta(n) for n in range(day_count)):
        single_date_str = single_date.strftime('%Y-%m-%d')
        url = f'https://gjbdsng.hvkfjdv.22'
        response_result.append(pool.apply_async(requests.get, [url], callback=_on_success, error_callback=_on_error))
    
    result_convert = []
    for result in response_result:
        json_result = json.loads(result.get().text) 
        app_id = json_result.get("app_id")
        date_convert = json_result.get("date_backfill")
        game_code = 'fksdnf'
        if(app_id == 'cfjfsalfas'):
            game_code = 'fsndf'
        url_convert = f'https://gjbdsng.hvkfjdv'
        result_convert.append(pool.apply_async(requests.get, [url_convert], callback=_on_success_convert, error_callback=_on_error_convert))
    
    for resd in result_convert:
        json_result_convert = resd.get().text
        print(json_result_convert)

start_date = (datetime.now() - timedelta(days=30)).date()
end_date = (datetime.now() - timedelta(days=1)).date()
app_id = 'cfjfsalfas'

_call_requests_parallel(start_date, end_date, app_id)