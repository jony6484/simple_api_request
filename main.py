import os, json, requests, shutil
from datetime import date, datetime, timedelta


API_URL = 'https://api.nasa.gov/planetary/apod'
APPID = '5fywSL7w0zAT991GDuZTtlsC3lWauWDrjCbfR90T'

def get_img(pic_date):
    # dt = str(date.today())
    params = {'api_key': APPID, 'date': pic_date}
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    pyVal = json.loads(response.text)

    if pyVal['media_type'] == 'image':
        local_dir = os.path.join('./data')
        dt_obj = datetime.strptime(pic_date, "%Y-%m-%d")
        dt_str = dt_obj.strftime("%Y_%m_%d")
        out_filename = os.path.join(local_dir, dt_str + '__' + 'nasa_daily.jpg')
        response = requests.get(pyVal['url'], stream=True)
        with open(out_filename, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response


if __name__ == '__main__':
    n=1
    start_date = datetime.today() - timedelta(days=n)
    pic_dates = [start_date + timedelta(days=dd) for dd in range(n) ]

    for dt in pic_dates:

        pic_date = dt.strftime("%Y-%m-%d")
        get_img(pic_date)

#



