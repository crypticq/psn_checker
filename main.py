

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': '*/*',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://id.sonyentertainmentnetwork.com/',
    'Authorization': 'Bearer 12345678-1234-1234-1234-123456789111',
    'X-Psn-Platform': 'WEB',
    'X-Psn-Account-Country': 'FR',
    'Content-Type': 'application/json; charset=utf-8',
    'X-Psn-Request-Id': '0',
    'X-Psn-Trace-Id': '0',
    'X-Psn-Span-Id': '0',
    'X-Psn-Sampled': '0',
    'Origin': 'https://id.sonyentertainmentnetwork.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

username = input("Enter Online ID: ")

c = {'onlineId' : username, 'reserveIfAvailable' : False}
response = requests.post("https://accounts.api.playstation.com/api/v1/accounts/onlineIds", json=c , headers=headers)
if response.status_code == 201:
    print(username , "is not taken")
