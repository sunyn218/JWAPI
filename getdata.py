import yaml
import requests

class Getdata():
    def getdata(self, filename, key):
        with open(f'../{filename}.yaml', encoding='utf-8') as f:
            return yaml.safe_load(f)[key]

    def send_data(self, filename, key, value):
        with open(f'../{filename}.yaml', 'w', encoding='utf-8') as f:
            yaml.dump({key:value}, f)

# data=Getdata()
# print(data.getdata("token", "token"))
