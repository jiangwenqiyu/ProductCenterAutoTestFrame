import requests


class RequestSend:

    def request(self, method, url, header, **kwargs):
        with open('record.txt', 'a') as f:
            f.write(method + '\n' + url + '\n' + str(header) + '\n' + str(kwargs))

        res = requests.request(method, url, headers = header, **kwargs)
        return res





