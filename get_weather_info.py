from pprint import pprint
import requests

from get_time import get_base  # 추가

def get_info():
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

    serviceKey = "/RiLDbQOrX1DYkcfCT5/LyQYEKJ3G4If9ktXL8/B8o3aCQfi/S6D0g+OFjWQD+dZa2ru1Iwbasb9TV+IlJU0wA=="

    base_date, base_time = get_base()  # 추가

    params = {
        'serviceKey': serviceKey,
        'pageNo': '1',
        'numOfRows': '1000',
        'dataType': 'JSON',
        'base_date': base_date,  # 변경
        'base_time': base_time,  # 변경
        'nx': '89',
        'ny': '90'
    }

    res = requests.get(url=url, params=params)
    res = res.json()
    data = res['response']['body']['items']['item']

    _data = []

    for d in data:
        _data.append((d['category'], d['obsrValue']))

    _data = _data[:4]

    code = {'PTY': '강수형태', 'REH': '습도', 'RN1': '1시간 강수량', 'T1H': '온도'}
    rain_info = ['없음', '비', '비/눈', '눈', '', '빗방울', '빗방울눈날림', '눈날림']

    weather_info = {}
    for c, v in _data:
        # 에러가 발생하면 해당 문구를 보내준다.
        try:
            v = rain_info[int(v)] if c == 'PTY' else float(v)
        except:
            return "데이터 준비 중입니다. 잠시 후 접속해주세요."

        weather_info[code[c]] = v

    return weather_info

if __name__ == "__main__":
    pprint(get_info())