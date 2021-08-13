import datetime

from django.contrib.sites import requests

from users.models import ExtendUser


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oath2':
        return


    api_url = f'https://api.vk.com/method/users.get/?fields=bdate.sex.about&acces token={response["acces_token"]}&v=5.92'

    response = requests.get(api_url)

    if response.status_code !=200:
        return

    data = response.json()['response'][0]

    if 'sex' in data:
        user.extenduser.gender

    if 'sex' in data:
        if data['sex'] == 1:
            user.extenduser.gender = ExtendUser.FEMALE
        elif data['sex'] == 2:
            user.extenduser.gender = ExtendUser.MALE

    if 'about' in data:
        user.extenduser.about_me = data['about']

    if 'bdate' in data:
        bdate = datetime.strptime(data['bdate'], "%d.%m.%Y")
        age = datetime.now().year - bdate.year
        user.age = age

    user.save