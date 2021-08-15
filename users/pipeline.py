import datetime
from urllib.parse import urlunparse, urlencode
from collections import OrderedDict

from django.contrib.sites import requests

from geekshop import settings
from users.models import ExtendUser


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oath2':
        return

    api_url = urlunparse(('https',
                        'api.vk.com',
                        '/method/users.get',
                        None,
                        urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'photo_max_orig')), acces_token=
                            response['acces_token'], v='5.92')),
                        None
                        ))

    response = requests.get(api_url)
    if response.status_code != 200:
        return

    data = response.json()['response'][0]
    if data['sex']:
        user.extenduser.gender = ExtendUser.MALE if data['sex'] == 2 else ExtendUser.FEMALE


    if 'photo_max_orig' in data:
        print(data['photo_max_orig'])
        photo_content = requests.get(data['photo_max_orig'])
        with open(f'{settings.MEDIA_ROOT}/users_images/{user.pk}.jpg', 'wb') as photo_file:
            photo_file.write(photo_content.context)
            user.image = f'users_images/{user.pk}.jpg'

    if data['about']:
        user.extenduser.about_me = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], "%d.%m.%Y")
        age = datetime.now().year - bdate.year
        user.age = age

    user.save
