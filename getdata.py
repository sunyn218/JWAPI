import yaml


class Getdata():
    def getdata(self, filename, key):
        with open(f'/Users/sunyanan/PycharmProjects/JWAPI/{filename}.yaml', encoding='utf-8') as f:
            return yaml.safe_load(f)[key]

    def send_token(self, filename, key, value):
        with open(f'/Users/sunyanan/PycharmProjects/JWAPI/{filename}.yaml', 'w', encoding='utf-8') as f:
            yaml.dump({key:value}, f)
# data=Getdata()
# print(data.getdata("token", "token"))
