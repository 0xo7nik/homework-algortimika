import requests
import json

data = {'login': 'shedrinm', 'name': 'Михаил Сергеевич', 'message': input('Введите сообщение: ')}

request = requests.post('http://algo.enotit.space/tion/api.php', data=data).content
