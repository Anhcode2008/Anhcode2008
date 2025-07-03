import requests
import json
class TraoDoiSub_Api(object):

    def __init__(self, username, password, proxy=None) -> None:
        self.username = username
        self.password = password
        self.proxies = None
        self.session = requests.Session()
        self.headers = {'authority': 'traodoisub.com', 'accept': 'application/json, text/javascript, */*; q=0.01', 'cache-control': 'max-age=0',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'origin': 'https://traodoisub.com', 'referer': 'https://traodoisub.com/', 'x-requested-with': 'XMLHttpRequest'}
        if proxy:
            try:
                proxy_parts = proxy.strip().split(':')
                if len(proxy_parts) == 4:
                    host, port, user, password = proxy_parts
                    self.proxies = {'http': f'http://{user}:{password}@{host}:{port}',
                                    'https': f'http://{user}:{password}@{host}:{port}'}
            except Exception as e:
                print(f'Lỗi khởi tạo proxy: {str(e)}')
                self.proxies = None

    def info(self):
        response = self.session.post('https://traodoisub.com/scr/login.php', headers=self.headers, data={
                                     'username': self.username, 'password': self.password}, proxies=self.proxies)
        if 'success' in response.text:
            self.cookie = response.headers['Set-cookie']
            headers = {'authority': 'traodoisub.com', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'en-US,en;q=0.9', 'cookie': self.cookie, 'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                       'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49', 'x-requested-with': 'XMLHttpRequest'}
            response = self.session.get(
                'https://traodoisub.com/view/setting/load.php', headers=headers).json()
            self.token = response['tokentds']
            self.xu = response['xu']
            self.name = response['user']
            return (True, self.name, self.xu, self.token)
        else:
            return (False, None)

    def facebook_configuration(self, id):
        try:
            response = self.session.post('https://traodoisub.com/scr/datnick.php',
                                         headers=self.headers, data={'iddat': id}, proxies=self.proxies).text
            return True if '1' in response else False
        except:
            return False

    def add_uid(self, id, g_recaptcha_response):
        headers = {'authority': 'traodoisub.com', 'accept': 'application/json, text/javascript, */*; q=0.01', 'accept-language': 'en-US,en;q=0.9', 'cookie': self.cookie, 'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"',
                   'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49', 'x-requested-with': 'XMLHttpRequest'}
        response = self.session.post('https://traodoisub.com/scr/add_uid.php', headers=headers, data={
                                     'idfb': id, 'g-recaptcha-response': g_recaptcha_response}, proxies=self.proxies).text
        if 'success' in response:
            return (True, None)
        elif 'error' in response:
            return (False, response)
        else:
            return response

    def get_g_recaptcha_response(self, apikey):
        try:
            response = requests.get(
                'https://traodoisub.com/view/cauhinh/', headers=self.headers, proxies=self.proxies)
            if response.status_code != 200:
                print('Lỗi khi lấy sitekey!')
                return (False, None)
            sitekey = response.text.split('data-sitekey="')[1].split('"')[0]
            captcha_solver = NextCaptcha(apikey)
            success, task_id = captcha_solver.recaptchav2(
                sitekey, 'https://traodoisub.com/view/cauhinh/')
            if success:
                success, g_recaptcha_response = captcha_solver.get_result(
                    task_id)
                if success:
                    return (True, g_recaptcha_response)
        except:
            return (False, 'Lỗi khi lấy reCAPTCHA')

    def get_nv_vip(self, fields, type):
        try:
            list_nv = self.session.get(
                f'https://traodoisub.com/api/?fields={fields}&access_token={self.token}&type={type}', proxies=self.proxies).json()
            return list_nv
        except:
            return False

    def get_nv_thuong(self, fields):
        try:
            list_nv = self.session.get(
                f'https://traodoisub.com/api/?fields={fields}&access_token={self.token}', proxies=self.proxies).json()
            return list_nv
        except:
            return False

    def get_xu_vip(self, type, id):
        try:
            get_xu = self.session.get(
                f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}', proxies=self.proxies).json()
            return get_xu
        except:
            return False

    def get_xu_thuong(self, type, id):
        try:
            get_xu = self.session.get(
                f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}', proxies=self.proxies).json()
            return get_xu
        except:
            return False

    def cache(self, type, id):
        try:
            cache = self.session.get(
                f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}', proxies=self.proxies).json()
            return cache
        except:
            return False
